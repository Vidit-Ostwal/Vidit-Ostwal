# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/1882#issuecomment-2701818692) in [crewAIInc/crewAI] on 2025-03-05.
  > *AI Summary: @Vidit-Ostwal has suggested attempting the process with the newest version of the software or tool in question. He mentions having attempted to reproduce a specific issue or behavior but was unsuccessful in doing so. The suggestion implies that updating to the latest version may resolve the problem encountered by the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2282#issuecomment-2701402365) in [crewAIInc/crewAI] on 2025-03-05.
  > *AI Summary: Vidit-Ostwal has suggested uncertainty regarding the matter at hand, suspecting that the root cause of the problem lies within LiteLLM, which is utilized internally. They came to this conclusion because they found the issue on reddit where other users of LiteLLM are facing a similar problem. The observation stems from*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2284#issuecomment-2701361461) in [crewAIInc/crewAI] on 2025-03-05.
  > *AI Summary: Vidit-Ostwal has suggested exploring the memory functionality available in CrewAI. The suggestion highlights the existence of a memory feature within CrewAI that could be beneficial. To understand this functionality, Vidit-Ostwal recommends checking the linked documentation. This documentation elaborates on the concept of memory within the CrewAI framework, providing insights into*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2696062734) in [crewAIInc/crewAI] on 2025-03-04.
  > *AI Summary: Vidit-Ostwal has suggested that they are attempting to assign `knowledge_sources` to an agent but are encountering a validation error during the crew's execution. The error indicates an invalid knowledge configuration, specifically requesting an OpenAI API key, even though a Gemini API key is being used. They noted that setting `knowledge_sources`*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2233#issuecomment-2695213518) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested clarification regarding knowledge source implementation within a task. The comment indicates that tasks should not directly incorporate any knowledge source. Instead, knowledge sources should be defined either at the crew level, affecting the entire team's operations, or at the individual agent level, tailoring resources to specific roles.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2234#issuecomment-2695204872) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that tasks, as they are currently defined, do not inherently accept knowledge as input. The user believes the issue likely arises from the manner in which knowledge sources are initialized. It's posited that the present structure doesn't naturally accommodate knowledge integration within tasks, implying a need for*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695052968) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested closing the current issue. The suggestion is based on confirmation that a previously discussed solution or approach was successful. With the positive verification, the original problem or concern that prompted the issue has been effectively addressed. The successful resolution eliminates the need for further investigation or action*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2255#issuecomment-2695021426) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: @Vidit-Ostwal has suggested encountering version conflicts while trying to add `google-generativeai` using `uv add`. The error indicates a failure to download and build `pypika==0.48.9` due to an incorrect length of an array when deserializing a cache entry. The error trace revealed that `pypika` was included as a dependency of `crewai`,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2260#issuecomment-2694784308) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested that the primary cause of an identified issue stems from an incorrect deep copy process related to the crew data. This improper handling occurs during each kickoff. The lack of a proper deep copy leads to unintended consequences. Specifically, this copying mechanism affects how crew data is*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2265#issuecomment-2694771952) in [crewAIInc/crewAI] on 2025-03-03.
  > *AI Summary: Vidit-Ostwal has suggested resolving issue #2260. The proposed solution involves addressing a problem related to the failure of an image pull policy. The original configuration resulted in images being pulled repeatedly, leading to inefficiency. To mitigate this, a new approach is recommended that modifies the image pull policy to `IfNotPresent`.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: Vidit-Ostwal has suggested that they are encountering an issue while trying to initialize knowledge in crewAI, despite having the `google-generativeai` package installed in their environment. They are attempting to adapt the `crewai_knowledge_getting_started` repository for use with Google AI Studio. The error log indicates a failure to initialize knowledge due to*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: @Vidit-Ostwal has suggested exploring the potential benefits of a Human Input Tool within the CrewAI framework. The tool would allow for intermediate human input through a web UI, enabling direct interaction between agents and humans after initial inputs are defined. This differs from a simple boolean flag. The core idea*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested there's an issue installing AutoGen in editable mode, encountering an error related to multiple top-level packages discovered in a flat-layout. This error prevents the build from proceeding, indicating a potential file structuring problem. They're seeking resources to understand and resolve this issue, as they haven't encountered it*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the crew fails when using `human_input` set to True due to issues with the `lite llm`. The problem occurs because the user role isn't being properly passed in the messages when `lite llm` is called. The provided code defines agents for Pokemon search, color validation, and*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested that when calling litellm with the google studio API, a "BadRequestError" is encountered, specifically a "VertexAIException". The error indicates that the "contents" are not specified in the GenerateContentRequest. This issue occurs while attempting to use the 'gemini/gemini-1.5-pro' model. The goal is to determine if user feedback requires*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: @Vidit-Ostwal has suggested incorporating the `.copy` method for the manager agent and the `shallow_copy` method for the manager LLM. This addition aims to improve the handling of agent and LLM configurations within the system. Specifically, it addresses the need for creating copies of these components. The inclusion of `.copy` and*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested an approach to address issue #2206, focusing on incorporating streaming functionality into the crewAI `llm` class. This involves modifying the class to include a `streaming = True` argument and ensuring it's passed during the `.call` function implementation. The object formed after each partial response should remain consistent*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The function was modified to retrieve the correct object, implying a previous error in object retrieval. This adjustment addresses a problem related to how crew data is accessed or utilized within the system. The specific implementation details of the*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2111, focusing on enhancing user feedback. The implemented solution includes adding a user message, formatted using the `feedback` mechanism. This improvement likely aims to provide clearer and more informative responses to user actions or system events. The goal is to ensure users receive*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: Vidit-Ostwal has suggested a fix for the issue reported in the discussion #2067. The proposed solution aims to resolve the problem that was previously identified. The user believes that the provided changes will effectively address the concerns raised in the earlier conversation. The intention is to offer a practical resolution*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
