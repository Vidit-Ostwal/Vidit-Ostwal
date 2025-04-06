# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that when initializing the `MDXSearchTool`, it's crucial to pass a `config` parameter. This configuration should be a dictionary that specifies the settings for both the Language Model (LLM) and the embedder. The LLM configuration should include details like the provider (e.g., Ollama, Google, OpenAI) and model name*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested improving the code's modularity and readability by breaking down lengthy functions into smaller, more manageable units. This would involve creating reusable functions that handle specific tasks, enhancing code maintainability and testability. The suggestion also includes a focus on optimizing conditional logic, aiming to simplify complex if/else structures*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested initializing each language model (LLM), but proposes initializing only one and assigning the same LLM to the others as a working alternative. In response to a query regarding the choice of OpenAI as the default LLM, Vidit-Ostwal has suggested that OpenAI's API gained prominence due to its*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested that users can define their own Large Language Models (LLMs) and integrate them into the crew by utilizing the 'llm' parameter. This allows for customization and flexibility in selecting the specific model that best suits the task requirements. Furthermore, a code snippet demonstrates how to instantiate an*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested following up on a previous interaction. The suggestion prompts a direct question regarding the success or failure of a prior recommendation or solution. The essence of the suggestion is to encourage feedback or confirmation from another user about whether a proposed action or solution effectively addressed their*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested a potential solution to address the reported issue. The suggestion involves updating the software or system to a newer version. This upgrade is recommended as a troubleshooting step to determine if the problem is related to an outdated version. It is a standard approach to resolving software*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested that the problem might be related to prompt engineering and proposes providing the language model with more information about the tool. To address this, they suggest replacing a specific function in the `base_tool.py` file with a revised version that offers enhanced details regarding the tool's functionality. The*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being utilized. An attempt was made to replicate the behavior using Gemini, but the issue was not observed in that environment. Therefore, understanding which LLM is in use is crucial for further investigation and potential resolution of the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a method for viewing the prompt sent to the language model (LLM) within the crewAI framework, noting that using verbose mode does not provide sufficient information. They identified the absence of a mechanism to directly inspect the final prompt before it's passed to the LLM. To address*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a system prompt design for an AI assistant specializing in people information retrieval. The prompt defines the assistant's role as a "People Information Specialist," its goal being to analyze questions, use provided tools to search for information about individuals, and provide concise summaries. If the question is*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested adding functionality to incorporate runtime data from Human through the command-line interface. The new feature enhances the system's capability to receive and process data during its operation, improving its real-time performance and adaptability. This enhancement offers users a more dynamic and interactive experience. The suggested functionality would*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: @Vidit-Ostwal has suggested adding a test case related to issue #2260. This addition aims to improve the project's testing coverage and ensure the reliability of the code concerning the identified problem. The test case contributes to a more robust and well-tested system. This addition is intended to prevent regressions and*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested modifications to address issue #2448, focusing on streamlining user memory configuration. The original code checked for both `self.memory_config` and `user_memory` within it. Vidit-Ostwal has suggested that it's sufficient to verify the existence of `memory_config` with "mem0" as the provider. The new implementation simplifies the logic, initializing `self._user_memory`*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when using tools within a crew with the `crewai run` command. The process of creating a virtual environment leads to `crewai_tools` being considered an optional dependency. The proposed solution addresses this by ensuring that `crewai_tools` is consistently installed, irrespective of*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the work done in issue #2422. The primary focus of this update is to refine the existing codebase by eliminating a specific test case that was deemed unnecessary. The removal aims to streamline the testing process and improve the overall efficiency of the project. This*

## ⭐ Starred Repositories
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
