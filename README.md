# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2696062734) in [crewAIInc/crewAI] on 2025-03-04.
  > *AI Summary: Vidit-Ostwal has suggested that they are attempting to assign `knowledge_sources` to an agent. They've provided code showing the agent definition with a specified knowledge source and embedding configuration. However, they are encountering a validation error during crew execution, indicating an issue with the knowledge configuration, specifically related to the absence*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2695213518) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested a clarification regarding knowledge source handling within the system. The existing task structure isn't designed to directly incorporate knowledge sources. Instead, knowledge should be defined and managed either at the crew level, representing a broader team or workflow, or at the individual agent level, allowing specific expertise*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2234#issuecomment-2695204872) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that tasks are not inherently designed to accept knowledge as a direct input. The comment focuses on how knowledge sources are being initialized within the system. The issue likely stems from the way these knowledge sources are set up and integrated into the task framework. Instead of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695052968) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested closing the current issue based on a confirmation of success. The original issue seems to have been resolved according to the reporter, and the suggested solution, whatever it might have been, apparently worked effectively. Therefore, since the problem that motivated the creation of the issue has been*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695021426) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that there was a version conflict encountered while adding the `google-generativeai` package using the command `uv add google-generativeai`. The error indicated a failure to download and build `pypika==0.48.9`, stemming from a deserialization issue with the cache entry, specifically an incorrect array length. The package `pypika` was included*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2260#issuecomment-2694784308) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the primary cause of an issue lies in the improper deep copy of the 'crew' data during each kickoff process. This inadequate deep copy mechanism leads to unintended data sharing or modification across different kickoff instances, creating inconsistencies and errors. The suggestion pinpoints the deep copy*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2265#issuecomment-2694771952) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested resolving issue #2260, focusing on improving code clarity and addressing potential edge cases. The suggestion involves a thorough review of the existing implementation, emphasizing the need for better documentation and more descriptive variable names to enhance code readability. Furthermore, it proposes implementing robust error handling mechanisms to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2241#issuecomment-2692131547) in [crewAIInc/crewAI] on 2025-03-01.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the LLM used for reproducing the error. Initially, there might have been a misunderstanding regarding the specific model, with mentions of both `llama3.2:latest` and `gemini-1.5-pro-latest`. However, @Vidit-Ostwal clarifies that the gemini model did not reproduce the error. The aim is to confirm the exact LLM being*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2691135574) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: Vidit-Ostwal has suggested a potential cause for an issue encountered while running `crewai`. The suggestion is that the virtual environment (venv) created during the `crewai run` process might be lacking the `google-generativeai` package. This absence within the venv could be the root of the problem. This package might be essential*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2689849315) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: @Vidit-Ostwal has suggested that upgrading to the newest version, specifically version 0.102.0, should resolve the reported error. Additionally, they mentioned ongoing efforts towards a more substantial update aimed at further refining AgentOps within the codebase. This comprehensive update is slated for release in the upcoming version. @Vidit-Ostwal inquired whether another*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: Vidit-Ostwal has suggested addressing an issue encountered while adapting a knowledge-based CrewAI setup for Google AI Studio. They are facing a persistent error where the knowledge initialization fails despite having the `google-generativeai` package installed in their environment. This issue arises when attempting to use the `gemini/gemini-1.5-pro` model. Vidit-Ostwal provided steps*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: Vidit-Ostwal has suggested the potential benefits of implementing a Human Input Tool. Such a tool would allow for intermediate requests for human input through a web user interface. This differs from a simple boolean setting, as it enables direct agent-human interaction during the process, rather than a pre-determined configuration. The*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered an error while trying to install AutoGen in editable mode, suspecting it's a file structuring issue. The error message indicates multiple top-level packages discovered in a flat-layout, preventing setuptools from building. They are seeking resources to better understand and resolve this problem. Vidit-Ostwal was*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested that the crew fails when `human_input` is set to True due to the missing user role in messages passed to the LiteLLM. The issue arises when user input is required, particularly in the `pokemon_color_validation_task`. The provided code sets up agents and tasks for Pokemon searching, color validation,*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested they encountered a "BadRequestError" while attempting to use the `litellm` library with the Google Studio API, specifically the "gemini/gemini-1.5-pro" model. The error message indicates that the "contents" field within the "GenerateContentRequest" is not being properly specified. They are using LiteLLM version 1.60.2. A code snippet illustrating their*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: @Vidit-Ostwal has suggested enhancements related to the manager agent and manager LLM within the codebase. Specifically, the suggestion involves incorporating `.copy` for the manager agent and `shallow_copy` for the manager LLM. This modification aims to improve the handling and manipulation of these components. The addition of `.copy` and `shallow_copy` likely*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested approaching issue #2206 by modifying the `llm` class in CrewAI to include a `streaming = True` argument, which would then be passed during the `.call` function's implementation. The aim is to yield consistent objects formed after a partial response and remove the return statement. A key question*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The original function was returning an incorrect object, leading to the reported problem. The suggested patch aims to correct this behavior by ensuring the function returns the expected and appropriate object. This adjustment is crucial for the proper functioning*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111. The solution involves adding a user message formatted using the `feedback` functionality. The focus is on providing clear and informative feedback to the user. The implemented change contributes to improved user experience by delivering well-formatted messages within the application. This enhancement ensures*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue detailed in the related issue report. This contribution aims to resolve the problem previously identified and discussed. The provided solution directly addresses the concerns raised in the linked issue, offering a targeted resolution. The implemented changes are intended to effectively mitigate the*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
