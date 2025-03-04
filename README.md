# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2696062734) in [crewAIInc/crewAI] on 2025-03-04.
  > *AI Summary: Vidit-Ostwal has suggested that they are encountering a validation error when assigning `knowledge_sources` to an agent. The error indicates an invalid knowledge configuration and suggests providing an OpenAI API key, despite the presence of a Gemini API key configuration. This issue arises during the agent initialization within the CrewAI framework.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2695213518) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that tasks should not be designed to directly incorporate knowledge sources. Knowledge integration, according to the suggestion, should be handled at either the crew level or the agent level. This approach provides a structured way to manage and utilize information within the system. By centralizing knowledge access*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2234#issuecomment-2695204872) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that the tasks are not defined to take knowledge as an input. The most probable reason for this behavior is likely related to how the knowledge sources are being initialized. The comment highlights a potential issue in the task definition or initialization process. This could be causing*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695052968) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested the issue can be closed because the solution has been verified. This confirms that the suggested approach successfully resolved the problem. The confirmation marks the completion of the issue and indicates that no further action is required. By closing the issue, it signifies that the problem is*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695021426) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that there were version conflicts encountered while attempting to add the `google-generativeai` package using the `uv add` command. The specific error involved the failure to download and build `pypika==0.48.9`, stemming from a deserialization issue within the cache. The error message indicated an incorrect array length, leading to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2260#issuecomment-2694784308) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the primary cause of an identified issue stems from an inadequate deep copy process applied to crew data during each kickoff. This improper deep copy leads to unintended data sharing or modification across different kickoff instances. Consequently, this shared data introduces inconsistencies and errors. Addressing this*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2265#issuecomment-2694771952) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested resolving issue #2260. The resolution involves addressing the current implementation's limitations and proposing a more efficient approach. The current method faces performance challenges due to its inefficiency. Vidit-Ostwal has suggested an alternative strategy to streamline the process and enhance performance. The focus is on leveraging a different*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2241#issuecomment-2692131547) in [crewAIInc/crewAI] on 2025-03-01.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the LLM used for reproducing the error, addressing a potential confusion. Initially, there was mention of using `llama3.2:latest`, while there was also reference to `gemini-1.5-pro-latest`. The suggestion aimed to confirm which model was accurately associated with the issue. Vidit-Ostwal clarified not being able to reproduce the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2691135574) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: Vidit-Ostwal has suggested a potential reason for an issue. They propose the problem might stem from the virtual environment (venv) created when running `crewai run` lacking the `google-generativeai` dependency. This missing package within the virtual environment could be the root cause of the observed malfunction. The suggestion highlights a possible*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2689849315) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: @Vidit-Ostwal has suggested that upgrading to the newest version, specifically version 0.102.0, should resolve the encountered error. The suggestion affirms a previous comment highlighting the same solution. Furthermore, they mention ongoing efforts to significantly improve AgentOps within the codebase. This enhancement is planned for release in the subsequent version. The*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: @Vidit-Ostwal has suggested an issue encountered while trying to integrate knowledge functionality with Google AI Studio, following a video tutorial. The problem arises during the initialization of knowledge, with a warning indicating that the `google-generativeai` package is not installed, despite it being present in the environment. To reproduce this, one*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: Vidit-Ostwal has suggested exploring the potential benefits of a Human Input Tool within the CrewAI framework. This tool would facilitate direct interaction between agents and humans through a web UI, enabling intermediate human input during processes. This approach differs from a simple boolean setting, as it allows for dynamic human*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested there's an issue installing AutoGen in editable mode, encountering an error during the process of obtaining the requirements to build editable version. The error indicates multiple top-level packages were discovered, leading to setuptools halting the build to prevent unintended file inclusion. Vidit-Ostwal believes this is related to*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested that when running a crew with `human_input` set to True, the process fails for any user-provided input. This issue arises because the lite LLM, when invoked, lacks the user role in the messages. They have included an image demonstrating this problem and provided code to reproduce it.*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested they encountered a `BadRequestError` while attempting to use the LiteLLM library with the Google Studio API. The error indicates that the `contents` field is not specified in the `GenerateContentRequest`. They are using LiteLLM version 1.60.2. The code snippet demonstrates an attempt to use the `completion` function with*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: @Vidit-Ostwal has suggested modifications to enhance the agent and language model (LLM) manager functionality. Specifically, they've incorporated `.copy` and `shallow_copy` to ensure proper handling of object states. The addition of `.copy` for the manager agent likely creates a new, independent instance, preventing unintended modifications to the original. The implementation of*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested implementing streaming functionality in the crewAI `llm` class by adding a `streaming = True` argument and passing it to the `.call` function. This approach involves modifying the `llm` class to handle streaming. The goal is to yield objects that are consistent with the current format after each*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The original function was not retrieving the correct object, leading to the reported problem. The suggested patch corrects this behavior, ensuring that the `get_crew()` function now returns the expected object. This fix addresses the core issue identified in the*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested a fix related to issue #2111. The changes involve incorporating a user message formatted using the `feedback` mechanism. The specific details of the original problem are not provided, but the solution focuses on enhancing user communication within the application. The goal is to provide more informative and*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: Vidit-Ostwal has suggested a resolution to the problem outlined in issue #2067. The proposed fix addresses the core concerns raised, offering a solution to the reported difficulties. This adjustment aims to rectify the identified fault and enhance the system's overall performance. The modification intends to eliminate the errors detailed in*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
