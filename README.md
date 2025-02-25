# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2207#issuecomment-2678315696) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal suggests a solution and asks for more information about structuring dependent files when creating an .exe file. They believe their suggested approach should work in most cases but would like to learn more about how dependent files were structured in previous .exe file creations.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1932#issuecomment-2678301644) in [explodinggradients/ragas] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested a change to `src/ragas/testset/transforms/default.py` where line 157 should be `Parallel(cosine_sim_builder, ner_overlap_sim)` instead of `ner_overlap_sim`. They have requested @rgrizzo-linksmt to raise a PR for this change.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2206#issuecomment-2677521676) in [crewAIInc/crewAI] on 2025-02-24.
  > *AI Summary: @Vidit-Ostwal has suggested revising the `.kickoff()` method to return a `CrewOutput` object. This object contains various attributes, including `raw`, `pydantic`, `json_dict`, and others. Vidit-Ostwal believes that this method could be enhanced by adding a yield feature that allows the output of each input case to be yielded as soon as*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2197#issuecomment-2676858424) in [crewAIInc/crewAI] on 2025-02-23.
  > *AI Summary: @Vidit-Ostwal has suggested that, for ease of reading, @chenggangqcg should share the bug in Python format.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1932#issuecomment-2676191712) in [explodinggradients/ragas] on 2025-02-22.
  > *AI Summary: @Vidit-Ostwal has suggested providing additional information about the problem being encountered. They recommend sharing details about the specific issue, including any error messages or exceptions that are occurring. This information would be helpful in diagnosing the problem and finding a solution.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1731#issuecomment-2676190883) in [explodinggradients/ragas] on 2025-02-22.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the code needed to reproduce @zoey-lyu's work. Sharing this code would be beneficial for those interested in replicating the results or further investigating the findings. It would also contribute to the transparency and reproducibility of the research, allowing others to build upon the work and potentially*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2051#issuecomment-2671690311) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has proposed guidelines for comment summarization. This includes summarizing the entire comment in 100 words, ignoring mentions and user tags, providing a summary from @Vidit-Ostwal's perspective, disregarding code examples but extracting key messages, and avoiding external links or code. All essential information should be included, and failure to adhere*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361982) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the query is within the scope of a flow. They have asked @lorenzejay to explain further since they are having difficulty understanding the context.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361167) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested using a Python script that recursively searches for a file named "crew.py" within the current directory and all its subdirectories. This script operates independently of the crewai project structure.*
- [Commented](https://github.com/microsoft/autogen/issues/5591#issuecomment-2666323375) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested an alternative approach for cloning the autogen repo. This solution would allow the repo to be used in an environment while also enabling modifications and edits. No specific details or code examples were provided in the comment.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal has discovered an error when attempting to install autogen in editable mode. The error message indicates that multiple top-level packages were discovered in a flat-layout, preventing automatic discovery from proceeding. They believe this is due to a file structuring issue. They have requested resources to better understand the error*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested to add feedback in the user role when the lite llm is called. This is because the problem with the provided code is that the lite llm doesn't have the user role in the messages, which leads to incorrect results. By adding feedback in the user role,*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal suggests that a `BadRequestError` is thrown when attempting to call the 'litellm' model with Google's `studio` API. The error message indicates that the request is missing the 'contents' field. He has provided a code example of the API call he's making, along with the error message he's receiving.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested a bug in setting up Langfuse via Docker Compose. The issue arises because port 9000, used by both ClickHouse and MinIO, is already in use by another system process. Despite attempts to change the port, the issue persists due to internal port usage. The comment includes an*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the CrewAI documentation should replace the parameter `model` with `model_name` in the sample code examples for using Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings. This change would align with the expected behavior of the code and improve the accuracy of the*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to obtain the correct object.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message that is formatted by `feedback`. This change addresses a previously reported concern.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. However, the comment does not provide any specific details about the nature of the issue or the solution implemented.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested updates to address the memory reset issue reported in issue #2023. These changes include eliminating the CLI command for memory reset and updating the documentation. However, additional modifications are deemed necessary. Namely, removing the CLI command and adjusting the documentation. These proposed changes are contingent upon alignment*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the documentation issue reported in GitHub issue #2030. This suggestion is made in response to an existing GitHub issue and aims to address a specific documentation-related problem. The suggestion does not include any specific code details or external references and is focused on resolving the reported*

## ⭐ Starred Repositories
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.
- Starred [huggingface/datatrove](https://github.com/huggingface/datatrove) on 2025-02-20.
- Starred [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) on 2025-02-20.
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.
- Starred [dhealy05/frames_of_mind](https://github.com/dhealy05/frames_of_mind) on 2025-02-18.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
