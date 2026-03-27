"""
Fluff Generator Module

Generates post-battle fluff based on the ongoing story and sides involved in battles.
This module provides functions for generating Warhammer 40k campaign narrative.

Features:
- Loads ongoing story context from text file
- Uses LangChain with Google Gemini API for narrative generation
- Maintains conversation history
- Includes relevant story context with each generation
"""

from langchain.messages import AIMessage, HumanMessage, SystemMessage
from typing import List, Dict, Optional
import logging

from . import model_funcs, prompts, retrieval

logger = logging.getLogger(__name__)


class FluffGenerator:
    """Handles generation of Warhammer 40k battle fluff using Claude/Gemini."""

    def __init__(self, debug_mode: bool = False):
        """
        Initialize the Fluff Generator.

        Args:
            debug_mode: Whether to enable debug logging
        """
        self.debug_mode = debug_mode
        self.model = None
        self._initialize_model()

    def _initialize_model(self):
        """Initialize the LLM model."""
        try:
            self.model = model_funcs.gemini_model()
            logger.info("Fluff generator model initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize model: {e}")
            raise

    def get_initial_messages(self) -> List[Dict]:
        """
        Get initial system and AI messages for a new conversation.

        Returns:
            List of initial messages for conversation history
        """
        return [
            prompts.system_message,
            prompts.ai_message
        ]

    def generate_response(
        self,
        user_message: str,
        message_history: Optional[List[Dict]] = None
    ) -> Dict[str, any]:
        """
        Generate a response to a user message about the campaign.

        Args:
            user_message: The user's question or battle report
            message_history: Previous conversation messages (optional)

        Returns:
            Dictionary containing:
                - 'response': Generated narrative text
                - 'messages': Updated message history
                - 'error': Error message if generation failed (optional)
        """
        try:
            # Initialize history if not provided
            if not message_history:
                message_history = self.get_initial_messages()

            # Validate input
            if not user_message or not user_message.strip():
                return {
                    'error': 'Empty message provided',
                    'messages': message_history
                }

            # Add user message to history
            message_history.append(HumanMessage(content=user_message))

            # Get relevant story context
            try:
                relevant_history = retrieval.extract_relevant_history(user_message)
            except Exception as e:
                logger.warning(f"Failed to retrieve story context: {e}")
                relevant_history = "Story context unavailable."

            # Prepare messages for model
            messages_for_model = message_history + [
                HumanMessage(
                    content=f"The relevant history is: {relevant_history}"
                )
            ]

            if self.debug_mode:
                logger.debug(f"Generated {len(messages_for_model)} messages for model")

            # Generate response
            try:
                response = self.model.invoke(messages_for_model)
                response_text = response.content
            except Exception as e:
                logger.error(f"Model generation failed: {e}")
                response_text = f"Error generating response: {str(e)}"

            # Add assistant response to history
            message_history.append({
                "role": "assistant",
                "content": response_text
            })

            if self.debug_mode:
                logger.debug(f"Response: {response_text[:100]}...")

            return {
                'response': response_text,
                'messages': message_history
            }

        except Exception as e:
            logger.error(f"Unexpected error in generate_response: {e}")
            return {
                'error': str(e),
                'messages': message_history or self.get_initial_messages()
            }

    def reset_conversation(self) -> List[Dict]:
        """
        Reset the conversation to initial state.

        Returns:
            Fresh initial message list
        """
        return self.get_initial_messages()

    def format_message_for_display(self, message: Dict) -> str:
        """
        Format a message for display purposes.

        Args:
            message: Message dict with 'role' and 'content'

        Returns:
            Formatted message string
        """
        role = message.get('role', 'unknown')
        content = message.get('content', '')

        if role == 'system':
            return f"[SYSTEM] {content}"
        elif role == 'assistant':
            return f"🤖 {content}"
        elif role == 'user':
            return f"👤 {content}"
        else:
            return content


# Convenience functions for direct use

_generator: Optional[FluffGenerator] = None


def get_generator(debug_mode: bool = False) -> FluffGenerator:
    """
    Get or create the global FluffGenerator instance.

    Args:
        debug_mode: Whether to enable debug logging

    Returns:
        FluffGenerator instance
    """
    global _generator
    if _generator is None:
        _generator = FluffGenerator(debug_mode=debug_mode)
    return _generator


def generate_fluff(
    user_input: str,
    history: Optional[List[Dict]] = None,
    debug: bool = False
) -> Dict[str, any]:
    """
    Generate fluff for the given user input.

    Args:
        user_input: User's question or battle report
        history: Previous message history
        debug: Enable debug logging

    Returns:
        Dictionary with 'response' and 'messages' keys
    """
    generator = get_generator(debug_mode=debug)
    return generator.generate_response(user_input, history)


def get_initial_state(debug: bool = False) -> List[Dict]:
    """
    Get initial conversation state.

    Args:
        debug: Enable debug logging

    Returns:
        Initial message list
    """
    generator = get_generator(debug_mode=debug)
    return generator.get_initial_messages()


def reset_generator_state(debug: bool = False) -> List[Dict]:
    """
    Reset the generator to initial state.

    Args:
        debug: Enable debug logging

    Returns:
        Fresh initial message list
    """
    generator = get_generator(debug_mode=debug)
    return generator.reset_conversation()


if __name__ == '__main__':
    # Example usage
    import json

    print("Initializing Fluff Generator...")
    generator = FluffGenerator(debug_mode=True)

    print("\n" + "="*60)
    print("Warhammer 40k Fluff Generator - Command Line Demo")
    print("="*60)

    messages = generator.get_initial_messages()

    print("\nInitial AI Message:")
    print(generator.format_message_for_display(messages[-1]))

    while True:
        print("\n" + "-"*60)
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye, Emperor protect!")
            break

        if user_input.lower() == 'reset':
            messages = generator.reset_conversation()
            print("Conversation reset.")
            continue

        print("\nGenerating response...")
        result = generator.generate_response(user_input, messages)

        if 'error' in result:
            print(f"Error: {result['error']}")
        else:
            print(f"\nAssistant: {result['response']}")
            messages = result['messages']
