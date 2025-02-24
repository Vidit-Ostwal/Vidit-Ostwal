# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2207#issuecomment-2678315696) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal suggests that the current implementation may mostly be functional. He inquires about the structure used for dependent files while creating the executable (.exe) file. He expresses gratitude for any insights into the file structuring process.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1932#issuecomment-2678301644) in [explodinggradients/ragas] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested a change in `src/ragas/testset/transforms/default.py`. Line 157 should be modified from `ner_overlap_sim` to `Parallel(cosine_sim_builder, ner_overlap_sim)`. They believe this change is appropriate and have requested that @rgrizzo-linksmt create a pull request to implement it.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2206#issuecomment-2677521676) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested investigating if yielding a `CrewOutput` object is possible when calling `.kickoff()` on the crew. Currently, `.kickoff()` returns a `CrewOutput` object, which contains the raw, pydantic, and JSON dictionary representations of the final task output, as well as the tasks' outputs, token usage, and other information. @Vidit-Ostwal believes*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2197#issuecomment-2676858424) in [crewAIInc/crewAI] on 2025-02-23.
  > *AI Summary: @Vidit-Ostwal has suggested converting the bug from the current format to a Python format for better readability. They believe that presenting the bug in Python format would make it more accessible and easier to comprehend.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1932#issuecomment-2676191712) in [explodinggradients/ragas] on 2025-02-22.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the problem being faced for better assistance. This information would enable the team to understand the specific challenge and provide tailored guidance or solutions.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1731#issuecomment-2676190883) in [explodinggradients/ragas] on 2025-02-22.
  > *AI Summary: @Vidit-Ostwal has suggested sharing code to reproduce @zoey-lyu's work. This will enable others to verify the results and build upon their findings. Sharing the code will contribute to transparency and reproducibility in the research community.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2051#issuecomment-2671690311) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested adding a few changes to improve the project's workflow: 1. Use Tuple classes instead of lists where possible. - This enables taking advantage of the built-in functions and operators of tuples, making the code more efficient. 2. Write unit tests for important functions. - This helps ensure*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361982) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal suggests that the topic of the flow should be clarified. They are unsure if it falls within the scope of the flow and would like further clarification from @lorenzejay.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361167) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested an independent script that recursively searches for a file named "crew.py" within all files and folders of the current directory. This script is not bound by the CrewAI project structure.*
- [Commented](https://github.com/microsoft/autogen/issues/5591#issuecomment-2666323375) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative methods for cloning the autogen repository. They are interested in using the repository within an environment while also maintaining the ability to make modifications and edits.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal has suggested that the error encountered during the installation of autogen in editable version is likely due to a file structuring problem. The error message indicates that multiple top-level packages were discovered in a flat layout, which can lead to accidental inclusion of unwanted files. To resolve this issue,*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested potential reasons why the code fails when running a crew with `human_input` set to True. According to @Vidit-Ostwal, the issue may arise due to the lite llm failing to receive the user role in the messages when called. To address this problem, @Vidit-Ostwal has recommended adding feedback*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that when trying to call the litellm library with Google Studio API, users may encounter a BadRequestError due to unspecified contents in the GenerateContentRequest.contents field. This issue has been observed while using version 1.60.2 of the litellm library.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that there's an issue when trying to set up langfuse via Docker Compose. The issue arises because port 9000, used by ClickHouse and MinIO, is already in use by another process that cannot be terminated. Changing the port in the configuration does not seem to resolve the*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the example code in the documentation for the "Memory" concept incorrectly uses the `model` parameter instead of the `model_name` parameter. This issue affects several examples across multiple pages:

- https://docs.crewai.com/concepts/memory
- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the issue #2123 by patching the `get_crew()` function to get the correct object.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message formatted by `feedback`. No further details about the code or the context of the fix were provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. The details of the fix are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the reset Memories issue raised in issue #2023. Additionally, they propose further improvements, including:

- Removing the CLI command for resetting Memories
- Making necessary documentation updates

They are willing to implement these changes if the proposed solution meets expectations.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the documentation issue mentioned in #2030.*

## ⭐ Starred Repositories
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.
- Starred [huggingface/datatrove](https://github.com/huggingface/datatrove) on 2025-02-20.
- Starred [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) on 2025-02-20.
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.
- Starred [dhealy05/frames_of_mind](https://github.com/dhealy05/frames_of_mind) on 2025-02-18.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
