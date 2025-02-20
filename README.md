# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361982) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the current conversation might be out of the scope of this particular workflow discussion, and has tagged @yqup to verify if that's the case. @Vidit-Ostwal has also requested @lorenzejay to provide further clarification on the topic.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2670361167) in [crewAIInc/crewAI] on 2025-02-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the file search feature operates independently of the CrewAI project structure. It recursively searches for a file named "crew.py" in all the files and folders within the current directory.*
- [Commented](https://github.com/microsoft/autogen/issues/5591#issuecomment-2666323375) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative methods to clone the autogen repo and utilize it within an environment. He inquires about the possibility of modifying and editing the repo while using it in a specific environment.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2665955523) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #1984 by fixing a bug. They believe this approach will address the reported issue effectively.*
- [Commented](https://github.com/microsoft/autogen/issues/5579#issuecomment-2665605410) in [microsoft/autogen] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested showing @fniedtner that they don't have access to the current page because their role only permits them to read the page. This can be done by changing the access restriction policy for their role and ensuring their role doesn't possess write permissions.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2664518371) in [crewAIInc/crewAI] on 2025-02-18.
  > *AI Summary: @Vidit-Ostwal has suggested using `crew.reset_memories('all')` as the simplest way to address the issue being discussed. They have added this suggestion to a pull request they have made and have also corrected the CLI command to retrieve the appropriate attribute.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested consolidating the codebase into a single file. They believe this would improve the organization and readability of the code. By centralizing the code, it may also make it easier to maintain and debug.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that @ashishpatel26 try updating the package because sessions are ending perfectly fine on their end.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to your case and could not be reproduced by them. They recommend checking the goals and description provided or trying to obtain the output in a different format, such as JSON, to troubleshoot the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether the file path where the crew is running aligns with the path in the terminal where `crewai reset-memories -a` is executed. This verification is crucial to ensure successful memory resetting.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: @Vidit-Ostwal has suggested that they encountered an error while trying to install autogen in its editable version using `pip install -e .`. The error message indicates a problem with the file structure, as multiple top-level packages were discovered in a flat layout. They believe this is a file structuring issue*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a possible solution to an issue where a crew with `human_input` set to True fails for any user input. The problem arises because lite llm is called without the user role in the messages. To resolve this issue, they have recommended adding feedback in the user role.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that the error encountered when using the LiteLLM API is due to an unspecified `contents` parameter in the `GenerateContentRequest`. They have provided a code example to illustrate the issue, which involves calling the `completion` function and specifying a model and message but omitting the `contents` parameter. The*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested to change the port number 9000, used by both Clickhouse and Minio containers, as it conflicts with a system process. Additionally, they have identified that internally, port 9000 is used elsewhere, causing the Clickhouse migrations to fail. They have expressed interest in contributing a fix for this*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the documentation for the CrewAI Memory concept, the parameter "model_name" should be replaced with "model" in all code examples. This is because the embedder takes the input of "model" instead of "model_name". The affected examples are found on the documentation pages for using Azure OpenAI*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function to retrieve the correct object. This change ensures that the function delivers accurate results.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message formatted by `feedback`. The fix includes both a frontend and a backend change, ensuring a consistent user experience across the platform. The frontend change involves displaying the user message in a consistent manner, while the backend change*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue discussed in pull request #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the reset memories issue reported in #2023. The suggested solution includes:

1. Removing the CLI command for resetting memories
2. Making necessary documentation changes

@Vidit-Ostwal is willing to implement these changes if they align with the overall solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit fixes documentation in response to the issue raised in #2030. No further details or references to specific code changes were provided in this comment.*

## ⭐ Starred Repositories
- Starred [unslothai/unsloth](https://github.com/unslothai/unsloth) on 2025-02-19.
- Starred [dhealy05/frames_of_mind](https://github.com/dhealy05/frames_of_mind) on 2025-02-18.
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
