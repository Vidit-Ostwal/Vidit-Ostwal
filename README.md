# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2696062734) in [crewAIInc/crewAI] on 2025-03-04.
  > *AI Summary: Vidit-Ostwal has suggested that they are attempting to assign `knowledge_sources` to an agent. They are encountering a validation error related to an invalid knowledge configuration. The error message indicates a missing OpenAI API key, even though they have configured an embedder with a Gemini API key. This issue arises when*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2695213518) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that tasks within the system are designed to operate without directly accessing external knowledge sources. Instead, knowledge integration should occur at either the crew level or the individual agent level. This design choice centralizes knowledge management, preventing tasks from independently seeking information. By restricting tasks in this*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2234#issuecomment-2695204872) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the current task definitions do not appear to be designed to explicitly receive knowledge as an input. This observation points to a potential issue in the way knowledge sources are being initialized. The focus should be on reevaluating the task definitions to ensure they are appropriately*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695052968) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that the proposed solution was successful. Consequently, they suggest that the current issue be closed. Their statement indicates a positive resolution to the problem addressed in the issue, confirming the effectiveness of the previously implemented fix or workaround. Their response signifies that the original problem has been*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695021426) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that there was a failure encountered while trying to add the `google-generativeai` package, specifically facing version conflicts. The error occurred during the download and build process of `pypika==0.48.9`, with a deserialization failure due to an incorrect array length. The package `pypika` was included as a dependency of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2260#issuecomment-2694784308) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that the issue primarily stems from an inadequate deep copy of the "crew" data during each kickoff process. This improper deep copy leads to unintended modifications and shared state between different kickoff instances. Because the crew object is not properly isolated, changes made in one instance inadvertently*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2265#issuecomment-2694771952) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2260. The suggestion involves addressing the current behavior and ensuring that a specific file's integrity is maintained throughout the process. This can be achieved by using a dedicated function. The function will verify the correctness of the file by comparing its hash with a calculated*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2241#issuecomment-2692131547) in [crewAIInc/crewAI] on 2025-03-01.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the specific LLM used for error reproduction. There seems to be a misunderstanding regarding the models mentioned. Initially, Llama3.2:latest was indicated as the model where the error was reproducible. However, there was also mention of Gemini-1.5-pro-latest. Vidit-Ostwal clarifies that the error was not reproducible with the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2691135574) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: Vidit-Ostwal has suggested a potential cause for an issue encountered while running `crewai`. The suggestion is that the virtual environment (venv) created during the `crewai run` process might be lacking the `google-generativeai` dependency. This absence of the `google-generativeai` package within the venv could be the reason behind the problem. The*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2689849315) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: @Vidit-Ostwal has suggested that updating to the latest version, specifically version 0.102.0, should resolve the reported error. It has been suggested that this update is a direct solution to the problem encountered. Additionally, @Vidit-Ostwal has informed that a more comprehensive update is in progress. This upcoming update aims to further*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: Vidit-Ostwal has suggested that they are encountering an issue while trying to initialize knowledge in crewAI with Google AI Studio compatibility. Despite having the `google-generativeai` package installed, they receive a warning stating it's not installed. This occurs when running a Crew that involves a User Understanding Assistant. They provided steps*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: Vidit-Ostwal has suggested exploring the potential benefits of a Human Input Tool that allows for intermediate human input via a web UI. This tool would enable direct interaction between agents and humans, differing from a simple boolean input. The idea is to create a system where human input can be*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered an error while attempting to install AutoGen in editable mode, suspecting a file structuring problem. The error arises during the process of obtaining requirements to build editable versions, indicating multiple top-level packages found in a flat-layout. Setuptools halts the build to prevent unintended inclusion*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that a Crew setup with `human_input` set to True fails due to the `lite llm` not receiving the user role in messages. The issue occurs when a user provides input. The setup involves multiple agents specializing in Pokemon identification based on descriptions, color, and height. Tasks are*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered a `BadRequestError` while using `litellm` with the Google Studio API, specifically `gemini/gemini-1.5-pro`. They are using version `1.60.2` of `litellm`. The error indicates that `GenerateContentRequest.contents` is not specified, even though they provided a messages array. The code attempts to call the `completion` function with a*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: @Vidit-Ostwal has suggested incorporating `.copy` and `shallow_copy` methods into the manager agent and manager LLM, respectively. This modification aims to enhance the handling and manipulation of these components within the system. The inclusion of these methods likely provides functionality for creating copies of the agent and LLM, potentially for purposes*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested an approach to address issue #2206, focusing on enabling streaming within the crewai `llm` class. The proposal involves adding a `streaming = True` argument and passing it during the `.call` function implementation. The goal is to ensure that objects formed mid-response are consistent and yielded, replacing the*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The current implementation was modified to retrieve the correct object, addressing the underlying problem highlighted in the issue. This enhancement is intended to improve the accuracy and reliability of the function's output. This adjustment ensures that the function now*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2111, focusing on enhancing the user experience through improved message formatting. This enhancement involves utilizing the `feedback` mechanism to format user messages, aiming to provide clearer and more informative feedback to users. The primary goal is to ensure that users receive well-structured and*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: Vidit-Ostwal has suggested a fix for the issue described in issue #2067. The proposed solution addresses the problem reported in the referenced issue, aiming to resolve the reported bug or enhancement request. The fix implements changes to the code to correct the identified problem. The implemented solution provides a direct*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
