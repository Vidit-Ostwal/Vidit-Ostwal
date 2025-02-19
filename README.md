# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2664518371) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested using `crew.reset_memories('all')` as the simplest way to reset all memories. This has been implemented in a PR and the CLI command has been fixed to fetch the correct attribute.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code for better understanding.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue with session ending unexpectedly may be due to an outdated package. They recommend updating the package to resolve the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: Vidit-Ostwal has suggested that you may not be able to reproduce the issue due to it being specific to your case. They recommend that you check the goals and description you have given, or try getting the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether the file path where the user's crew is running and the path in the terminal where they are executing the `crewai reset-memories -a` command are the same. This will help ensure that the command is targeting the correct crew.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying if a particular observation also gets appended to the Python output. They are seeking confirmation on this matter.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that @joaomdmoura merge this current piece of work.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, alongside parent agents. The tool should be capable of initiating a crew, which would be managed by a parent crew. This would provide a hierarchical structure for managing crews and agents within the tool.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that instead of using pre-computed settings or a generic manager, it would be more beneficial to have direct control over the settings. They believe this approach offers more flexibility and allows for better customization according to specific requirements.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after a task has been performed to ask for feedback on the generated response. They recommend providing all necessary input during the `crew.kickoff()` rather than adding it mid-execution.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a solution to fix the issue where the crew fails for any user input when human_input is set to True. The problem arises because the lite llm is not assigned the user role in the messages. To resolve this, feedback should be added in the user role.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that while using LiteLLM's Python API, they encountered a "BadRequestError" when calling the completion function. The error message indicates that the "contents" parameter in the "GenerateContentRequest" was not specified. They have provided a code snippet that demonstrates their attempted API call and the error they received. Additionally,*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the langfuse docker setup is failing due to port 9000 being used by another process. They have attempted to change the port, but believe it is also used internally elsewhere. They have provided an error message and are seeking guidance on where to make the necessary*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the provided documentation links contain an error. The 'embedder' function takes the input of 'model' instead of 'model_name'. This issue needs to be fixed to align with the description provided in the documentation.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format support to the logging file to make it parsable for further analysis. This would also partially address issue #1970. They propose modifying the `output_log_file` to support both .txt and JSON formats. They are willing to contribute a pull request for this implementation.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123. They have applied a patch to the `get_crew()` function to ensure it retrieves the correct object.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111. The fix involves adding a user message formatted by "feedback". The specific details of the code implementation are not provided in the comment. However, it is clear that the fix addresses the issue and provides a formatted user message using the "feedback"*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. This change addresses the reported problem and should resolve the issue mentioned in the original thread.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the reset memories issue reported in #2023. To implement this fix, the CLI command for resetting memories will be removed. Additionally, documentation updates are necessary to reflect these changes. @Vidit-Ostwal is available to make these modifications if the proposed solution is acceptable.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this change fixes the documentation issue raised in #2030. No other relevant information was provided in the comment.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
