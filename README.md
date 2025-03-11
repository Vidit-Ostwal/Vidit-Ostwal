# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2323#issuecomment-2712558515) in [crewAIInc/crewAI] on 2025-03-11.
  > *AI Summary: Vidit-Ostwal has suggested confirming the functionality of normal litellm calls. The user tested litellm independently and confirmed its proper operation. The user has defined the llm backend for their agent. However, there appear to be issues when integrating litellm with the agent setup, despite its independent functionality. The user aims*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2323#issuecomment-2712545138) in [crewAIInc/crewAI] on 2025-03-11.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the method used to call litellm with the specific model "Claude Sonnet 3.7 Thinking." Understanding the implementation details of this integration is of interest. The focus is on grasping the practical steps and commands involved in invoking litellm with the mentioned Claude Sonnet model. This*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2315#issuecomment-2711305609) in [crewAIInc/crewAI] on 2025-03-10.
  > *AI Summary: Vidit-Ostwal has suggested trying a solution to address an issue. They are currently unable to test the solution themselves due to another problem they are facing. Vidit-Ostwal requests that someone else test the suggested approach. The purpose of this testing is to determine whether the proposed solution effectively resolves the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2315#issuecomment-2711290893) in [crewAIInc/crewAI] on 2025-03-10.
  > *AI Summary: Vidit-Ostwal has suggested there might be an issue within the documentation. Specifically, they propose passing an embedder directly to the crew. Their reasoning is that knowledge sources generally require an embedder for internal storage purposes. To address this potential problem and improve the documentation's clarity, they plan to create a*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2299#issuecomment-2708734819) in [crewAIInc/crewAI] on 2025-03-09.
  > *AI Summary: Vidit-Ostwal has suggested that a solution might be working, involving the creation of a session and changes to a crew. The session was created using AWS credentials. The crew was modified to include the created session within its configuration. This involves specifying a session for a Bedrock embedder. However, Vidit-Ostwal*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2299#issuecomment-2708734402) in [crewAIInc/crewAI] on 2025-03-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the reported problem might be related to the "memory" function issue, echoing concerns raised by other users. This connection implies a potential underlying cause affecting multiple functionalities. Understanding the root cause of this issue could help fix other related problems. This might be a duplicate issue*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2706538369) in [crewAIInc/crewAI] on 2025-03-07.
  > *AI Summary: Vidit-Ostwal has suggested considering Devin's workaround. More broadly, Vidit-Ostwal is interested in understanding the reasoning behind the large number of arguments the LLM generates before invoking a tool. Vidit-Ostwal proposes an experiment involving swapping the current LLM with a different one. The goal is to determine whether the issue stems*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2299#issuecomment-2706530675) in [crewAIInc/crewAI] on 2025-03-07.
  > *AI Summary: @Vidit-Ostwal has suggested passing a session key within the config attribute. This involves modifying the configuration by including a session object, created using `boto3.Session`, specifying the profile name and region. The suggestion aims to configure the embedder with session details, likely to manage authentication or regional settings for the Bedrock*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1998#issuecomment-2706313002) in [crewAIInc/crewAI] on 2025-03-07.
  > *AI Summary: Vidit-Ostwal has suggested updating the crew version and trying again. This suggestion aims to address an unspecified issue or potential bug encountered during the usage. The focus is on leveraging a newer version of the crew to potentially resolve the problem. By updating, the system can benefit from the latest*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1866#issuecomment-2704446036) in [crewAIInc/crewAI] on 2025-03-06.
  > *AI Summary: Vidit-Ostwal has suggested that the issue stems from using the incorrect parameter name, specifically "query," instead of the intended "sql_query" when interacting with the tool. To resolve this, they recommend updating the version to incorporate the correction. By ensuring the correct parameter is utilized, the functionality should align with expectations*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: @Vidit-Ostwal has suggested that they are encountering issues with initializing knowledge when trying to adapt the crewai_knowledge_getting_started repository for Google AI Studio. Despite having the `google-generativeai` package installed, a warning message indicates that the package is missing, preventing knowledge initialization. The provided code snippet showcases modifications to the `crew.py` file,*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: Vidit-Ostwal has suggested the potential benefits of a Human Input Tool. This tool would act as an intermediary, requesting human input via a web UI during the operation of an AI system. This is different from a simple boolean input, offering more interactive control. The proposed tool enables agents to*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered an error while trying to install AutoGen in editable mode using `pip install -e .`. The error indicates multiple top-level packages were discovered, causing the build to fail. This is likely a file structuring problem. Vidit-Ostwal seeks resources to understand and resolve this issue,*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that running a crew with `human_input` set to True fails because the lite LLM isn't given the user role in the messages. The problem occurs when the user provides input. The agents are defined for Pokemon search, color validation, and height validation. Tasks are defined for each,*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested debugging an issue encountered while using the LiteLLM library with the Google Gemini API, specifically Gemini 1.5 Pro. The user is facing a "BadRequestError," with the error message indicating that "contents is not specified" in the GenerateContentRequest. The user provided a code snippet demonstrating how they are*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2317) in [crewAIInc/crewAI]: Fixed no embedder in documentation issue. (2025-03-10).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue number 2315. The suggestion indicates a fix has been implemented for this specific problem. While the details of the issue and the precise solution are not elaborated upon, the main point is that a resolution has been proposed. The provided information suggests a targeted approach*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2312) in [crewAIInc/crewAI]: Pr branch (2025-03-08).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2307, building upon the work in #2309. The proposed solution addresses the need to handle two types of crew initialization. This includes scenarios where a crew is directly instantiated, for example, through the creation of a direct instance of a Crew object. The*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: Vidit-Ostwal has suggested incorporating `.copy` and `shallow_copy` functionalities into the codebase. This enhancement aims to refine the management of agent and language model (LLM) components within the system. The addition of `.copy` for the manager agent intends to create independent duplicates, preventing unintended modifications to the original agent. Conversely, the*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested initial thoughts regarding issue #2206. The suggestion involves modifying the crewai `llm` class by adding a `streaming = True` argument and passing it during the `.call` function implementation. This approach aims to ensure that objects formed after a partial response are consistent with the current state, yielding*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by patching the `get_crew()` function. The update aims to correct the object retrieval process within the function, ensuring it now returns the appropriate data. This adjustment is intended to address a specific problem related to how `get_crew()` currently operates. The proposed fix focuses on*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
