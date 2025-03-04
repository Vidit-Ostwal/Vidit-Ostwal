# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2696062734) in [crewAIInc/crewAI] on 2025-03-04.
  > *AI Summary: Vidit-Ostwal has suggested there's a validation error when assigning `knowledge_sources` to an agent. The error indicates an invalid knowledge configuration, specifically requesting an OpenAI API key, despite the user setting the key. This issue arises when defining the agent within the crew setup. However, setting `knowledge_sources` at the crew level*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2695213518) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that tasks should not inherently incorporate knowledge sources directly. Instead, the implementation should consider defining knowledge sources either at the crew level or at the agent level. This approach promotes a more modular and organized structure for managing and accessing information. This suggestion clarifies the architecture, ensuring*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2234#issuecomment-2695204872) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that tasks are not designed to accept knowledge as direct input. The issue likely stems from the way knowledge sources are being initialized. The task's purpose is to perform operations, not to directly handle knowledge injection. The focus should be on correctly initializing knowledge sources, rather than*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695052968) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested closing the issue, confirming that the proposed solution or previous actions effectively resolved the problem. The confirmation implies a successful resolution, validating the implemented fix or adjustment. This resolution suggests that no further action is required regarding this specific issue, streamlining the project workflow by indicating task*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695021426) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that they encountered version conflicts while trying to add the `google-generativeai` package using `uv`. The error occurred during the download and building of `pypika==0.48.9`, specifically related to deserializing a cache entry with an incorrect array length. This package was included due to a dependency chain involving `simple-knowledge-example`,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2260#issuecomment-2694784308) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the root cause of an issue lies in an incorrect implementation of a deep copy operation concerning crew data during each kickoff process. This flaw potentially leads to undesired data sharing or modification across different kickoff instances. The improper deep copy of the crew could lead*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2265#issuecomment-2694771952) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2260. They emphasized the importance of addressing this issue, outlining a strategy to ensure a comprehensive solution. They highlighted key areas within the issue that require specific attention and careful consideration. The suggested approach involves a systematic review of the problem, followed by the implementation*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2241#issuecomment-2692131547) in [crewAIInc/crewAI] on 2025-03-01.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the LLM used for error reproduction. There seems to be a misunderstanding regarding which model was used. Initially, it was mentioned that the error could be reproduced with `llama3.2:latest`, but there was a later reference to `gemini-1.5-pro-latest`. To resolve the confusion, clarification on the specific LLM*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2691135574) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might stem from the virtual environment (venv) created during the execution of `crewai run`. Specifically, the necessary package, `google-generativeai`, might be absent within this venv. This absence could potentially lead to errors or unexpected behavior during the crewai execution. Investigating whether the virtual environment*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2689849315) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: Vidit-Ostwal has suggested that updating to the latest version, specifically version 0.102.0, should resolve the encountered error. The user agreed with this suggestion, indicating it should eliminate the issue. Furthermore, Vidit-Ostwal mentioned that a more substantial update is in progress. This upcoming update aims to further refine and clean up*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: @Vidit-Ostwal has suggested encountering an issue while trying to integrate knowledge functionality with Google AI Studio, after following a video tutorial. Despite having the `google-generativeai` package installed, the system throws a warning indicating it's missing during knowledge initialization. After cloning a repository and modifying the `crew.py` file to align with*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: Vidit-Ostwal has suggested exploring the potential benefits of a Human Input Tool, which would allow for intermittent human interaction through a web UI. This differs from a simple boolean flag and enables direct agent-human communication once initial inputs are established, preventing interference during the process. The tool aims to facilitate*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested there's an issue installing AutoGen in editable mode, encountering an error related to multiple top-level packages during the build process. The error arises due to the file structure, preventing setuptools from proceeding with the build, and suggests exploring custom discovery, src-layout, or explicitly setting `py_modules` or `packages`.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested there's an issue when running a crew with `human_input` set to True, as it consistently fails with user-provided input. The root cause seems to be that LiteLLM isn't receiving the correct user role in the messages. Vidit-Ostwal provided a code example defining agents (Pokemon specialists) and tasks*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered a `BadRequestError` while using LiteLLM with the Google Studio API, specifically with the `gemini/gemini-1.5-pro` model. The issue arose when attempting to call the LiteLLM completion function. Vidit-Ostwal provided the code snippet used, highlighting the model specification, messages, and API key setup. The error message*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: @Vidit-Ostwal has suggested updates concerning the copying mechanisms employed for manager agents and language models. Specifically, the `.copy` method has been implemented for the manager agent, indicating a full, independent duplication of the object and its associated data. In contrast, a `shallow_copy` method is suggested for the manager language model.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested approaching issue #2206 by modifying the crewai `llm` class to include a `streaming = True` argument, and subsequently passing this argument during the `.call` function implementation within the class. This involves ensuring that the object created after receiving a partial response remains consistent with the current one,*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The function was modified to ensure it retrieves the correct object, addressing the problem outlined in the issue. This update rectifies a flaw in the original implementation, promising more accurate and reliable retrieval of crew-related data. The fix directly*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested addressing issue #2111 by incorporating user feedback. The contribution focuses on enhancing the user experience through improved messaging. Specifically, the change involves formatting user messages using a `feedback` function or mechanism. This formatting aims to present information to users in a clear, concise, and easily understandable manner.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: Vidit-Ostwal has suggested a fix for the issue reported in issue #2067. The fix addresses the problem identified in the mentioned issue, aiming to resolve it. This contribution seeks to improve the project's overall functionality and stability by directly tackling the reported bug. The suggested changes are intended to eliminate*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
