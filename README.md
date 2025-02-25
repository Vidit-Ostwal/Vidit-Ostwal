# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI-tools/issues/223#issuecomment-2679221846) in [crewAIInc/crewAI-tools] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested referring to a related issue (#2209) for further details on a different issue that inspired his suggestion.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2209#issuecomment-2679194991) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested making significant revisions to the code, including removing asyncio, the answer question queue, and other elements. These changes aim to streamline and improve the code's functionality.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2209#issuecomment-2679150186) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested using an image to visually represent the guidelines for summarization. The image provides a clear and concise overview of the key points to keep in mind when summarizing comments, including the word limit, perspective, handling of code examples, and exclusion of external links. This visual aid effectively*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2209#issuecomment-2679140315) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might not be reproducible as they were able to replicate the same scenario in a different project and it worked as expected. They have shared a link to a repository where the issue is not occurring.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2207#issuecomment-2678315696) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal suggests that the provided solution is likely to be effective and inquires about the structuring of other dependent files during the creation of the .exe file. They express gratitude for the assistance provided.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1932#issuecomment-2678301644) in [explodinggradients/ragas] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested that in `src/ragas/testset/transforms/default.py`, line 157 should be `Parallel(cosine_sim_builder, ner_overlap_sim)` instead of `ner_overlap_sim`. This makes sense and @rgrizzo-linksmt should raise a PR for this.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2206#issuecomment-2677521676) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal suggested considering the option of yielding the `CrewOutput` object returned by `.kickoff()` on the crew. This would allow for the output of an input case to be yielded as soon as it becomes available, rather than waiting for all input cases to finish. The `kickoff_for_each` and `kickoff_for_each_async` functions could*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2197#issuecomment-2676858424) in [crewAIInc/crewAI] on 2025-02-23.
  > *AI Summary: @Vidit-Ostwal has suggested that converting the bug report into a Python format would make it easier to read. The user believes that the Python format will provide a clearer and more concise representation of the issue, allowing for a better understanding of the bug's behavior and impact.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1932#issuecomment-2676191712) in [explodinggradients/ragas] on 2025-02-22.
  > *AI Summary: @Vidit-Ostwal has suggested that the original author of the issue should provide more context about the problem they are facing. The author is requested to provide a detailed description of the issue to allow for better understanding and resolution.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1731#issuecomment-2676190883) in [explodinggradients/ragas] on 2025-02-22.
  > *AI Summary: @Vidit-Ostwal has suggested sharing code to reproduce the results of @zoey-lyu. This would assist in further analysis and troubleshooting any issues or limitations in the code.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: @Vidit-Ostwal suggests exploring the benefits of implementing a Human Input Tool. This tool would differ from the `human_input = True` setting by enabling human collaboration within an agent's execution. Through a web UI, this tool would solicit human input during agent operation, allowing humans to interact directly with agents and*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal has suggested that the error encountered during the installation of autogen in editable version is due to a file structuring problem. The error message indicates that multiple top-level packages were discovered in a flat-layout, which setuptools considers a potential unintended inclusion. @Vidit-Ostwal suggests exploring custom discovery options, using a*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a solution to an issue where a crew with `human_input` set to True fails for any user input. The issue arises because the lite LLM in use lacks the user role in messages. To resolve this, the feedback should be added in the user role.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the `completion` function parameters. The error indicates that the `contents` parameter is missing. Adding `'contents':'...'` to the function call should resolve the issue.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the error "failed to open database" while setting up Langfuse via docker-compose is due to port 9000 being used by another process. They have tried changing the port but believe it is also being used internally. They are seeking assistance in identifying all necessary port changes*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to retrieve the correct object.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested fixing issue #2111 by adding a user message formatted by `feedback`. This change addresses an existing problem and aims to improve the user experience by providing a clear and customized message. By incorporating this fix, the overall functionality and user satisfaction of the platform will be enhanced.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. Unfortunately, the comment does not provide any further details about the nature of the fix or the approach taken to resolve the issue.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the memory reset issue raised in #2023. The proposed solution also includes:

- Removing the CLI command to reset memories
- Making necessary documentation changes

@Vidit-Ostwal has expressed willingness to implement these additional changes if the solution aligns with the project's requirements.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the documentation issue mentioned in Issue #2030. These changes have been implemented in this commit.*

## ⭐ Starred Repositories
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.
- Starred [huggingface/datatrove](https://github.com/huggingface/datatrove) on 2025-02-20.
- Starred [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) on 2025-02-20.
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
