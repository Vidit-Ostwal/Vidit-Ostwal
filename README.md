# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361982) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue is within the scope of a flow. They have tagged @yqup for confirmation. Additionally, @lorenzejay has requested clarification on the issue, but @Vidit-Ostwal has expressed difficulty in understanding @lorenzejay's explanation.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361167) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the search for the file "crew.py" should be independent of the crewai project structure. The search should recursively look for the file in all the files and folders of the current directory.*
- [Commented](https://github.com/microsoft/autogen/issues/5591#issuecomment-2666323375) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested an alternative method to simultaneously clone, modify, and edit the autogen repo: - Clone the repo as a submodule within another project - Make the necessary modifications - Commit the changes to the submodule - Push the changes to the parent repository - This allows users to*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2665955523) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested closing the issue #1984 as fixed. They have tested the changes and confirmed that the issue is resolved. No further actions are required on this issue.*
- [Commented](https://github.com/microsoft/autogen/issues/5579#issuecomment-2665605410) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested showing @fniedtner that they don't have access to this page.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2664518371) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested a simple approach to reset all memories using `crew.reset_memories('all')`. They have implemented this solution in a pull request and have also fixed the CLI command to retrieve the correct attribute.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code in one place for ease of reference.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the sessions end perfectly fine for them and recommends updating the package to resolve the issue encountered by @ashishpatel26.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that you re-examine the goals and description provided for the task. Additionally, it's recommended to attempt obtaining the output in an alternative format, such as JSON, to determine if the issue is specific to your case.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming that the file path where the crew is running is the same as the path in the terminal where you are executing `crewai reset-memories -a`. This is to ensure that the correct memories are being reset.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal has suggested that the error occurs when attempting to install autogen in an editable version using `pip install -e .`. The error message indicates that multiple top-level packages were discovered in a flat layout, causing setuptools to fail the build. This suggests that the file structure may be causing*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue where crew fails to filter Pokemon candidates based on their color attributes when `human_input` is set to True. The problem arises because the lite LLM is not given the user role in the messages. To resolve this, they recommend adding feedback in*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested looking into the error message received when calling the LiteLLM API. The error indicates that the 'contents' field in the 'GenerateContentRequest' object is missing. To resolve this, ensure that the 'contents' field is specified before making the API request. Additionally, no relevant log output was provided for*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the port 9000 used by both ClickHouse and MinIO is already in use on their system. They have tried to change the port, but believe that it is also used internally somewhere else. After making these changes, they encountered an error applying ClickHouse migrations, potentially due*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the input parameter for the embedder in the documentation for various embeddings, such as Azure OpenAI, Google AI, Vertex AI, and Cohere, is incorrectly specified as `model` instead of `model_name`. They have provided links to the relevant documentation pages for reference.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to retrieve the correct object. The specific code details of the patch are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that Pull Request #2111 has been fixed by adding a user message formatted by "feedback." This resolution addresses the issue reported in the original pull request.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. The specific details of the fix have not been provided in this comment, but it can be assumed that the changes address the issue raised in the referenced issue. Further information can be found by reviewing the commits associated*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for an issue mentioned in #2023, where memories would not reset properly. Additionally, they have identified the need for further modifications: 1. Removing the CLI command used for memory resets 2. Updating the documentation to reflect these changes @Vidit-Ostwal is willing to implement these changes if*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue that was reported in issue #2030. The proposed fix involves updating the documentation to provide more detailed instructions, optimize the format for better readability, and correct any errors or inconsistencies. By addressing these issues, the improved documentation aims to enhance its*

## ⭐ Starred Repositories
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.
- Starred [dhealy05/frames_of_mind](https://github.com/dhealy05/frames_of_mind) on 2025-02-18.
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
