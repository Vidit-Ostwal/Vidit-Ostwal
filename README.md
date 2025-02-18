# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2664518371) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested the simplest solution is to use `crew.reset_memories('all')`. This suggestion has been implemented in a pull request and the CLI command has been fixed to retrieve the correct attribute.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be helpful to have the complete code shared in one place, for easier reference and understanding.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that @ashishpatel26 try updating their package to potentially resolve an issue where the session is not ending correctly. According to @Vidit-Ostwal, the session ends as expected on their end, so the issue may be specific to @ashishpatel26's configuration or package version.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the error might be specific to the user's case. They recommend checking the goals and description, or trying to get the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether the file path where your crew is running and the path in the terminal where you are executing `crewai reset-memories -a` are the same. This is to ensure the reset command is executed in the correct directory to effectively reset crew memories.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that @ninad-opsverse's observation should be checked. Specifically, @Vidit-Ostwal has remarked on whether the output of a given action also includes an appended portion relevant to their discussion.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew inside a tool, along with parent agents. The tool should have the ability to kick off a crew, which will be managed by a parent crew. This approach allows for a hierarchical structure within the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests using a generalized manager instead of pre-computed data. They believe that having control over the data is preferable, especially when managing complex systems where adaptability is crucial.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after a task is performed to request feedback on the generated response. He discourages incorporating additional context during crew execution and recommends providing all necessary input during `crew.kickoff()` to avoid cluttering the crew execution process.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that while running a crew with `human_input` set to true, the lite llm in the crew fails to give the user role in the messages when called. This occurs due to the lack of role assignment in the messages, as illustrated in the attached screenshot. The code*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested checking a potential issue with the provided code snippet while calling the litellm API. The error encountered is a BadRequestError, indicating that the request is missing a required parameter, specifically the `contents` field in the `GenerateContentRequest`. The summary further mentions that the LiteLLM version being used is*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested changes to the Langfuse docker setup to address the issue where port 9000 is already in use. They found the port is used by both Clickhouse and Minio, preventing the setup from running. They have attempted to change the port setting but believe it is also used*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the CrewAI documentation for using different embeddings should be updated to use the `model_name` parameter instead of the `model` parameter. Specifically, the following pages in the documentation should be updated: - Using Azure OpenAI Embeddings - Using Google AI Embeddings -*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON output format to the logging file, which is currently limited to a .txt format that is difficult to parse. This suggestion aligns with issue #1970. Additionally, @Vidit-Ostwal has expressed willingness to contribute a pull request for this implementation.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to retrieve the appropriate object. They have implemented this fix and provided a patch for review.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111. The user message will now be formatted by the `feedback` function. This change addresses the issue where the user message was not being formatted correctly.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. The details of the fix are not provided in this comment, but it is likely that the changes address the issue described in the referenced issue. Once the issue is resolved, the fix will be merged into the main*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the memory reset issue raised in #2023. Additional modifications are required, including removing the CLI command for memory reset and updating documentation. @Vidit-Ostwal can implement these changes upon confirmation of solution alignment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. This fix ensures that the documentation accurately reflects the current functionality of the codebase. By addressing this discrepancy, the documentation will provide a more reliable and up-to-date guide for users, reducing confusion and improving overall usability.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
