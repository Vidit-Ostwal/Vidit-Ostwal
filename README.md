# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2696062734) in [crewAIInc/crewAI] on 2025-03-04.
  > *AI Summary: @Vidit-Ostwal has suggested that there is a validation error occurring when trying to assign `knowledge_sources` directly to an agent. The specific error encountered is a `ValidationError` related to an "Invalid Knowledge Configuration," indicating a requirement for an OpenAI API key. This arises despite an attempt to configure an embedder with*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2695213518) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that tasks are not designed to directly incorporate knowledge sources. The appropriate levels for defining knowledge sources are either at the crew level or at the individual agent level. This design choice emphasizes a separation of concerns, preventing tasks from being tightly coupled with specific knowledge repositories.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2234#issuecomment-2695204872) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the current task definitions might not be designed to directly receive knowledge as an input. They believe that the initialization of knowledge sources is the most likely reason for this behavior. The issue likely stems from how knowledge is being integrated or passed into the task*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695052968) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested closing the issue as the proposed solution worked. The original issue likely involved a problem or bug that needed resolution. The successful implementation of a fix or workaround has rendered the issue obsolete. Therefore, the suggestion is to mark the issue as resolved and prevent further discussion*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695021426) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested that running `uv add google-generativeai` resulted in version conflicts, specifically failing to download and build `pypika==0.48.9`. The error indicated a failure to deserialize a cache entry due to an incorrect array length. This dependency issue arose because `simple-knowledge-example` relies on `crewai`, which in turn depends on `chromadb`,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2260#issuecomment-2694784308) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that the primary cause of an issue stems from an incorrect deep copy process applied to the crew during each kickoff. This flawed deep copy implementation leads to unintended consequences and errors. It affects the consistency and isolation of crew data across different kickoff instances. To address*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2265#issuecomment-2694771952) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2260. They propose updating the text color of buttons that navigate to external websites. The goal is to improve visibility and usability, especially for users with visual impairments. They suggest that adjusting the text color will ensure sufficient contrast against the button's background, making the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2241#issuecomment-2692131547) in [crewAIInc/crewAI] on 2025-03-01.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the LLM used to reproduce the error. There seems to be a misunderstanding, as it was previously mentioned that the error could be reproduced using `llama3.2:latest`. However, it was later stated that the Gemini model did not produce the same error. Vidit-Ostwal clarifies that they were*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2691135574) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: @Vidit-Ostwal has suggested a potential reason for an issue encountered during the execution of `crewai run`. They propose the problem might stem from the virtual environment (venv) lacking the `google-generativeai` dependency. The virtual environment, which is created when the `crewai run` command is initiated, may not include the necessary `google-generativeai`*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2689849315) in [crewAIInc/crewAI] on 2025-02-28.
  > *AI Summary: @Vidit-Ostwal has suggested that updating to the latest version, specifically 0.102.0, should resolve the encountered error. Furthermore, a more substantial update is in progress, aimed at improving and cleaning up AgentOps within the codebase. This enhanced version is slated for release in the subsequent update. The suggestion focuses on resolving*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: Vidit-Ostwal has suggested investigating an issue encountered while adapting a CrewAI knowledge example for Google AI Studio. Despite having the `google-generativeai` package installed, the knowledge initialization fails, throwing a warning about the missing package. This issue arises when running the Crew setup after cloning a specified repository and modifying the*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: Vidit-Ostwal has suggested exploring the potential benefits of a "Human Input Tool" that allows for intermediate human interaction through a web UI. This tool would differ from simple boolean human input flags by enabling direct agent-to-human interaction. This approach aims to facilitate dynamic input and guidance from humans during automated*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested that an error occurs when attempting to install autogen in editable mode, version 0.7.4, using `pip install -e .`. The error indicates multiple top-level packages found in a flat layout, preventing setuptools from building. It suggests exploring custom discovery, a `src-layout`, or explicitly setting `py_modules` or `packages`.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested that the crew fails when `human_input` is set to True because the lite LLM isn't given the user role in the messages. The provided code defines agents for Pokemon search, color validation, and height validation, along with tasks that utilize these agents. The color validation and height*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered a `BadRequestError` while using the LiteLLM library with the Google Studio API. The user is attempting to call `litellm.completion` with the "gemini/gemini-1.5-pro" model. The messages include a system prompt. The user has provided the relevant traceback and the error message, indicating an issue with*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: @Vidit-Ostwal has suggested adding `.copy` for the manager agent and `shallow_copy` for the manager LLM. This modification aims to improve the handling of agents and language models within the manager component. The addition of `.copy` ensures that the manager agent is properly duplicated, preventing unintended modifications to the original agent.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested initial thoughts on issue #2206, focusing on implementing streaming capabilities within the crewAI framework. The proposed approach involves modifying the `llm` class to include a `streaming = True` argument and passing this parameter during the `.call` function implementation. The suggestion further highlights the need to ensure the*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The existing implementation incorrectly retrieved an object and the proposed patch aims to rectify this. This adjustment ensures that the `get_crew()` function now returns the accurate object, addressing the root cause of the problem described in issue #2123. By*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111, focusing on improving user feedback mechanisms. The enhancement involves adding a user message formatted using the `feedback` component. This addition is intended to provide clearer and more structured communication to the user. The primary goal of this modification is to ensure that*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: Vidit-Ostwal has suggested a resolution for the problem outlined in issue #2067. The proposed solution aims to address the reported bug or unexpected behavior by implementing a corrective measure. While specific implementation details are omitted, the focus is on rectifying the core issue described in the linked issue. The resolution*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
