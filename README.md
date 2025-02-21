# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2051#issuecomment-2671690311) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be beneficial to provide more detailed guidelines for the summarization task. This includes specifying the number of words to use for the summary (100 words), ignoring mentions and tagged users, and providing the summary from the perspective of the user who made the comment.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361982) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that this issue falls within the scope of a flow. They have tagged [@yqup](https://github.com/yqup) for confirmation. However, they have also expressed confusion about the context of the issue and have requested further clarification.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361167) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the search for the file called "crew.py" should be independent of the CrewAI project structure. The suggestion is to recursively search for the file within all the files and folders of the current directory.*
- [Commented](https://github.com/microsoft/autogen/issues/5591#issuecomment-2666323375) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested an inquiry regarding alternative methods to clone the autogen repo, utilize it in an environment, and modify it. The suggestion is directed specifically to @jackgerrits for further insights and potential solutions.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2665955523) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested closing the issue #1984 labeled "Fixed". They believe that the issue has been resolved and no further action is required.*
- [Commented](https://github.com/microsoft/autogen/issues/5579#issuecomment-2665605410) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested a change where the error message "showing you don't have access to this page" will be displayed for users who try to access a page they do not have access to. This will help clarify why the user cannot access the page and guide them to the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2664518371) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested that the simplest way to address this issue is to use `crew.reset_memories('all')`. They have added this to a PR and have also fixed the CLI command to fetch the desired attribute.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code in one place for easier reference and improved clarity. This would allow readers to have a comprehensive view of the code without having to search through multiple fragments.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the session ending issue might have been resolved by updating the package. This is because the commenter, @ashishpatel26, mentioned that the session ends perfectly fine for them, indicating that the issue may have been resolved on their end after updating the package.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue being faced might be specific to the user's case since they were unable to reproduce it. They recommend checking the provided goals and descriptions or trying to obtain the output in JSON format.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal has suggested that the error encountered during editable installation of autogen is likely due to a file structuring problem. The error message indicates that multiple top-level packages ('samples', 'packages', 'templates') were found in a flat-layout. To resolve this, they recommend setting up custom discovery or explicitly setting 'py_modules' or*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a possible solution for a problem where a crew fails to run with human_input set to True. The issue arises because lite llm doesn't receive the user role in the messages when called. To resolve this, they propose adding feedback in the user role.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that they are facing an error while calling litellm with the Google studio API. The error message indicates that the "contents" parameter is not specified in the GenerateContentRequest. To resolve this, they should ensure that the "contents" parameter is set in the request.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that port 9000, which is required for ClickHouse and MinIO, is already in use by another process that cannot be terminated. Changing the port in the Docker compose configuration is not enough, as other internal references to port 9000 may exist. They have encountered an error related*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for CrewAI's memory concepts needs to be updated. Specifically, the code examples provided in the documentation use "model" as the input parameter for the embedder instead of "model_name." This inconsistency should be corrected throughout the documentation, including the Azure OpenAI, Google AI, Vertex AI,*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to obtain the correct object. This solution has been implemented.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by incorporating user feedback into the message formatting via the `feedback` function. This change resolves the reported issue.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. The suggested changes aim to address the problem described in the issue, ensuring that the issue is resolved. By implementing these changes, the issue will be effectively fixed, enhancing the overall functionality and stability of the system. This fix*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes to address the reset memories issue raised in #2023. Beyond these fixes, @Vidit-Ostwal also proposes additional changes: 1. Removal of the CLI command for resetting memories 2. Updates to documentation @Vidit-Ostwal seeks confirmation that the proposed solution aligns with the desired approach before implementing these further*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. The suggested fix will resolve the issue and improve the documentation clarity.*

## ⭐ Starred Repositories
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.
- Starred [huggingface/datatrove](https://github.com/huggingface/datatrove) on 2025-02-20.
- Starred [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) on 2025-02-20.
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.
- Starred [dhealy05/frames_of_mind](https://github.com/dhealy05/frames_of_mind) on 2025-02-18.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
