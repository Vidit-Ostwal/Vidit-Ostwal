# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2051#issuecomment-2671690311) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested the following guidelines for comment summarization: - Summarize the entire comment in 100 words, capturing all important information. - Ignore @mentions and tagged users. - Provide the summary from "@Vidit-Ostwal has suggested" perspective. - Extract the key message from code examples without specific code details. - Avoid*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361982) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal seeks clarification from @lorenzejay regarding whether a particular issue falls within the scope of a flow. The commenter expresses difficulty understanding the context and requests further explanation.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361167) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the code should be independent of the crewai project structure. It will recursively search for a file named "crew.py" within all files and folders in the current directory.*
- [Commented](https://github.com/microsoft/autogen/issues/5591#issuecomment-2666323375) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative methods to clone the autogen repo. This would allow for its use in an environment while also enabling modifications and edits to the repository. @jackgerrits was mentioned as someone who may have insights on this matter.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2665955523) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested marking the issue as fixed and closing it. They have not provided any specific details about the fix, but they are confident that the issue has been resolved. They have also mentioned that tests have passed, indicating that the fix has been verified.*
- [Commented](https://github.com/microsoft/autogen/issues/5579#issuecomment-2665605410) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested showing @fniedtner that they do not have access to the current page. This information could be useful in troubleshooting access issues or determining appropriate permissions for the user.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2664518371) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested that the simplest approach to achieve the desired behavior is to use the `crew.reset_memories('all')` command. This suggestion has been implemented in a pull request and the CLI command has been fixed to retrieve the appropriate attribute.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be helpful if the entire code could be shared in one place, rather than being spread across multiple files or locations. This would make it easier to review and understand the codebase.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested investigating a potential issue with the package version being utilized. The commenter has encountered no difficulties with session termination, suggesting that the issue may be specific to the version of the package currently installed. Updating the package to its most recent version is recommended.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to the user's case, as they were unable to reproduce the error. They recommend checking the goals and description provided, or trying a different output format such as JSON.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal reported an error while attempting to install autogen in editable mode, resulting in the message "subprocess-exited-with-error." The error stems from multiple top-level packages discovered in a flat-layout, which setuptools deems inappropriate for automatic discovery. To resolve this, they suggest customizing discovery, using a src-layout, or explicitly setting packages with*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the code is failing because the `lite llm` is not given the user role in the messages when called. They have added feedback in the user role and recommend using the `add_feedback` method to provide a more comprehensive explanation. Additionally, they have suggested exploring alternative approaches,*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested reviewing an error encountered while calling the litellm API using the Google Studio API. The error is related to missing content specification in the GenerateContentRequest object. To resolve this, ensure that the "contents" field in the request object is populated. The code snippet provided in the comment*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the issue occurs when setting up langfuse via docker compose up because port 9000, used by both clickhouse and minio, is already in use by another system process. Changing the port in the configuration does not resolve the issue as the port is also used internally.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the "model" parameter in the sample code examples provided in the docs should be replaced with "model_name." This issue is present in the examples for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to retrieve the correct object. The issue involved retrieving an incorrect object using the `get_crew()` function. The patch applied by @Vidit-Ostwal rectifies this issue, ensuring that the function returns the intended object.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has fixed issue #2111. They have added a user message that is formatted by `feedback`. No further details were provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the reset memories issue reported in issue #2023. Their proposed solution involves:

1. Removing the CLI command for resetting memories.
2. Updating the documentation to reflect these changes.

@Vidit-Ostwal is willing to implement these changes if their solution aligns with the team's approach.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the documentation issue brought up in issue #2030 with this commit.*

## ⭐ Starred Repositories
- Starred [huggingface/datatrove](https://github.com/huggingface/datatrove) on 2025-02-20.
- Starred [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) on 2025-02-20.
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.
- Starred [dhealy05/frames_of_mind](https://github.com/dhealy05/frames_of_mind) on 2025-02-18.
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
