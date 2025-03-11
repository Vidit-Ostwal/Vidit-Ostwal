# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2323#issuecomment-2712558515) in [crewAIInc/crewAI] on 2025-03-11.
  > *AI Summary: Vidit-Ostwal has suggested focusing on the normal litellm call that has been working. They tested litellm independently and confirmed its proper functionality. They have defined the llm backend for their agent. They also mentioned they have configured a callback in the agent to print intermediate tool steps and llm thoughts.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2323#issuecomment-2712545138) in [crewAIInc/crewAI] on 2025-03-11.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific method being employed to invoke the litellm model, specifically when utilizing the "Claude Sonnet 3.7 Thinking" configuration. The request aims to gain insight into the practical implementation and setup used for integrating and interacting with the model. This information would potentially help to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2315#issuecomment-2711305609) in [crewAIInc/crewAI] on 2025-03-10.
  > *AI Summary: @Vidit-Ostwal has suggested a potential solution to the issue. Due to an unrelated problem hindering testing capabilities, they are unable to verify the effectiveness of the proposed solution themselves. They request that someone else try implementing the solution. Vidit-Ostwal is particularly interested in knowing whether this approach resolves the entire*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2315#issuecomment-2711290893) in [crewAIInc/crewAI] on 2025-03-10.
  > *AI Summary: Vidit-Ostwal has suggested there might be an issue with the documentation. The suggestion is to try passing an embedder directly within the crew. The reasoning is that any knowledge source generally requires an embedder because that's how data is internally stored. Therefore, providing the embedder at the crew level could*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2299#issuecomment-2708734819) in [crewAIInc/crewAI] on 2025-03-09.
  > *AI Summary: Vidit-Ostwal has suggested a potential solution involving the creation of a session using `boto3` with AWS credentials retrieved from environment variables. This session is then incorporated into the crew configuration, specifically within the embedder settings. The suggestion arises from the observation that the CrewAI framework might already establish a session*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2299#issuecomment-2708734402) in [crewAIInc/crewAI] on 2025-03-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the reported issue might be related to a previously observed problem concerning the "memory" function. He noted that others have also encountered and discussed this same issue. The suggestion implies a potential underlying cause or pattern connecting the current problem with previous reports involving memory-related operations.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2706538369) in [crewAIInc/crewAI] on 2025-03-07.
  > *AI Summary: Vidit-Ostwal has suggested exploring why the language model generates numerous arguments before invoking a tool. They concur with a prior suggestion but are particularly interested in identifying the cause of the excessive arguments. Vidit-Ostwal proposes testing a different language model to determine if the behavior is specific to the current*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2299#issuecomment-2706530675) in [crewAIInc/crewAI] on 2025-03-07.
  > *AI Summary: @Vidit-Ostwal has suggested exploring the inclusion of a session key within the config attribute. This addition aims to enhance the configuration options. The suggestion involves passing a session key in the config, which is expected to improve the flexibility and control over the setup process. @Vidit-Ostwal proposes a modification to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1998#issuecomment-2706313002) in [crewAIInc/crewAI] on 2025-03-07.
  > *AI Summary: Vidit-Ostwal has suggested updating the crew version and attempting the process again. This recommendation implies a potential issue with the current crew version being used. By updating to the latest version, it may resolve underlying problems or compatibility issues causing the initial failure. This troubleshooting step is crucial for ensuring*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1866#issuecomment-2704446036) in [crewAIInc/crewAI] on 2025-03-06.
  > *AI Summary: Vidit-Ostwal has suggested that an issue is occurring because the `query` parameter is being used instead of the expected `sql_query` parameter within a tool. They recommend updating the current version to address this parameter discrepancy. This update should involve ensuring the tool correctly utilizes the `sql_query` parameter for proper functionality.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2255) in [crewAIInc/crewAI]: [BUG] Issue while trying to initializing a google ai studio embedder in knowledge (2025-02-28).
  > *AI Summary: Vidit-Ostwal has suggested that they are encountering an issue while trying to initialize knowledge in a CrewAI setup, despite having the `google-generativeai` package installed. They are working to adapt the code for Google AI Studio compatibility, and have provided logs showing a warning about the package not being installed. They*
- Raised an [issue](https://github.com/crewAIInc/crewAI-tools/issues/223) in [crewAIInc/crewAI-tools]: Human Input Tool- Feature Request (2025-02-24).
  > *AI Summary: @Vidit-Ostwal has suggested exploring the potential benefits of a Human Input Tool integrated with web UI. This tool would facilitate direct agent-human interaction. Unlike a simple boolean flag, this proposed tool would enable dynamic human input during the process. This tool would serve as an intermediary, allowing agents to request*
- Raised an [issue](https://github.com/microsoft/autogen/issues/5591) in [microsoft/autogen]: Error while installing autogen in editable version (2025-02-18).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered an error while attempting to install AutoGen in editable mode, suspecting a file structuring issue. The error arises during the "getting requirements to build editable" stage, indicating multiple top-level packages found in a flat layout. Setuptools halts the build to prevent unintended file inclusion,*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: Vidit-Ostwal has suggested that the crew fails when `human_input` is set to True due to the LiteLLM not receiving the user role in messages. The issue arises with user-provided input. To reproduce, a crew is defined with three agents specializing in Pokemon search, color validation, and height validation, respectively. Tasks*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: Vidit-Ostwal has suggested that they encountered a "BadRequestError" while attempting to call litellm with the Google Studio API. They are using litellm version 1.60.2. The error message indicates an "INVALID_ARGUMENT" because "contents is not specified" in the GenerateContentRequest. The user provided a code snippet demonstrating their usage of the `litellm.completion`*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2317) in [crewAIInc/crewAI]: Fixed no embedder in documentation issue. (2025-03-10).
  > *AI Summary: Vidit-Ostwal has suggested a resolution for issue #2315. This contribution aims to address and rectify the problem outlined in the original issue report. The implemented solution focuses on resolving the core problem identified and improving the functionality or stability related to the issue. The provided fix has been tested and*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2312) in [crewAIInc/crewAI]: Pr branch (2025-03-08).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2307, building upon the progress made in #2309. The proposed solution focuses on accommodating different methods of crew initialization. This includes scenarios where a crew is directly instantiated as an object and instances where a function or class returns a crew object. The*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2265) in [crewAIInc/crewAI]: Added .copy for manager agent and shallow copy for manager llm (2025-03-03).
  > *AI Summary: Vidit-Ostwal has suggested implementing `.copy` for the manager agent and `shallow_copy` for the manager's language model. These additions aim to enhance the cloning or replication capabilities within the system. The `.copy` method will likely create a deep copy of the manager agent, ensuring that all its attributes and associated objects*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2247) in [crewAIInc/crewAI]: Adding streaming functionality, starting a discussion (2025-02-27).
  > *AI Summary: Vidit-Ostwal has suggested an approach to address issue #2206. The suggested approach involves modifying the `llm` class in `crewai` to include a `streaming = True` argument, which would then be passed to the `.call` function. This would enable the handling of streaming responses. A key consideration is ensuring the consistency*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving issue #2123 by implementing a patch within the `get_crew()` function. The patch aims to retrieve the correct object, implying that the original implementation was returning an incorrect or unexpected object. The modification focuses on ensuring the accurate retrieval of crew-related data. By patching the function, the*

## ⭐ Starred Repositories
- Starred [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) on 2025-03-01.
- Starred [agno-agi/agno](https://github.com/agno-agi/agno) on 2025-02-26.
- Starred [letta-ai/letta](https://github.com/letta-ai/letta) on 2025-02-25.
- Starred [langchain-ai/langmem](https://github.com/langchain-ai/langmem) on 2025-02-24.
- Starred [huggingface/picotron](https://github.com/huggingface/picotron) on 2025-02-20.

## 🍴 Forked Repositories
No repositories forked recently.
