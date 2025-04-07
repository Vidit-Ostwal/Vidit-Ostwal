# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested the necessity of passing a `config` parameter during initialization. The configuration should include details for both the Language Model (LLM) and the embedder. The LLM configuration should specify the provider, such as "ollama," along with model-specific configurations like the model name. Similarly, the embedder configuration should define*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested introducing comprehensive unit tests for the entire codebase, emphasizing their crucial role in maintaining code quality and preventing regressions. These tests should cover various scenarios and edge cases to ensure robustness. Furthermore, the suggestion encompasses thorough documentation of all functions and classes, highlighting the importance of clear*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested that initializing each Large Language Model (LLM) is necessary, but a practical tip is to initialize one and then assign the others to the same LLM, which should work effectively. Addressing the question of why OpenAI is the default LLM, they explained that OpenAI's API was adopted*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested that users can define their own Large Language Models (LLMs) and integrate them into the crew by using the `llm` parameter. This allows for customization and flexibility in selecting the desired LLM for specific tasks within the crew. While a link to documentation with Google LLM setup*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested inquiring about the success of a previous suggestion or solution. The comment seeks to confirm whether a proposed approach, likely discussed earlier in the thread, effectively addressed the user's issue. The intention is to follow up and provide further assistance if needed. The comment reflects a proactive*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested upgrading the version to potentially resolve the issue. By updating to a newer version, any existing bugs or incompatibilities present in the current version might be addressed, leading to improved functionality or stability. This action aims to eliminate the problem encountered and ensure proper operation. It's a*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested that the issue lies in prompt engineering and proposes providing the language model with more information about the tool to potentially resolve the problem. A specific solution involving a function replacement in the `base_tool.py` file within the crewAI repository has been suggested. The purpose of the proposed*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being used. They indicated that they experimented with Gemini and did not encounter the problem being discussed. The comment aims to identify if the issue is specific to a particular LLM implementation by inquiring about the model in use.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a method to view the final prompt sent to the language model. Observing that the verbose option doesn't provide sufficient information, they propose printing the prompt immediately before the call to the LLM. To achieve this, they added a print statement within the `crew_agent_executor.py` file, specifically targeting*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested providing a detailed system message and instructions for an AI assistant designed to be a People Information Specialist. The assistant's primary goal is to answer questions about individuals by using a specified search tool to find information within a JSON file. The instructions emphasize that the AI*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested adding functionality to incorporate runtime data from Human through the Command Line Interface (CLI). This enhancement provides a new way to integrate data. The commenter also anticipates expanding this functionality further by incorporating WebSockets. This future addition will likely enable real-time data streaming and bidirectional communication. This*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: @Vidit-Ostwal has suggested adding a test case related to issue #2260. The purpose of this addition is to ensure that the application does not crash under specific circumstances, thereby improving its robustness and stability. This test case focuses on handling a scenario where a key property is missing, which previously*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested changes to address issue #2448, focusing on streamlining the user memory configuration. The initial code checked for both `memory_config` and `user_memory` within it. The revised logic simplifies this by primarily verifying the existence of `memory_config`. Instead of raising a `TypeError`, the updated code initializes `self._user_memory` using `Memory()`*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when using tools within a crew via the `crewai run` CLI command. This process establishes a virtual environment that incorrectly recognizes `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes that `crewai_tools` should be installed universally, irrespective of whether*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the work done in issue #2422. The comment indicates a continuation of efforts related to a previous task or feature. Specifically, the suggestion focuses on refining an existing set of tests. According to the commenter, an unnecessary test case has been removed. This modification aims*

## ⭐ Starred Repositories
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
