# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that the `MDXSearchTool` initialization requires a `config` parameter. This configuration should be a dictionary containing settings for both the language model (`llm`) and the embedding model (`embedder`). For the language model, specify the `provider` (e.g., "ollama") and a nested `config` dictionary with the `model` name (e.g., "llama2")*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested implementing a solution using either an in-memory or Redis-based store. This choice depends on the scale, with in-memory being suitable for smaller deployments and Redis for larger ones needing persistence and scalability. The proposed solution focuses on avoiding common issues like duplicate requests. It also considers the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested that initializing each language model (LLM) is necessary, proposing a method where only one is initialized, and others are assigned to it, suggesting that this approach should be effective. They explained that OpenAI's API was chosen as the default LLM due to its early adoption and widespread*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested defining a custom Large Language Model (LLM) and incorporating it into the crew using the `llm` parameter. This allows users to specify their preferred LLM for task execution within the crew framework. The configuration involves setting parameters like the model name (e.g., "gemini/gemini-1.5-pro-latest") and temperature (e.g., 0.7)*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested a follow-up inquiry regarding a previously discussed solution. The suggestion aims to ascertain the efficacy of a proposed method. It is intended to gather feedback and confirm whether the aforementioned solution has been successfully implemented and resolved the issue for the user. This inquiry seeks to determine*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested a potential solution to an issue. The suggestion involves upgrading the version of a particular software or library. The user is advised to perform this upgrade. Following the upgrade, the user should retry the operation or process that previously encountered a problem. This approach is recommended as*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested that the problem might be related to prompt engineering. He proposes a solution focused on providing the language model with more information about the tool, even though he's currently unable to reproduce the error. He suggests replacing a specific function in the `base_tool.py` file with a modified*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being utilized. He mentioned attempting the same task with the Gemini LLM and reported not encountering a similar problem. Therefore, understanding the particular LLM in use is essential to identify potential discrepancies or issues unique to that model, aiding*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a method to view the prompt sent to the LLM, noting that verbose mode doesn't provide sufficient information. They point out the absence of a direct way to see the final prompt before it's passed to the language model. To address this, they implemented a solution by*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested that the prompt defines a "People Information Specialist" AI assistant. The AI's primary function is to find and summarize information about people using specific tools. The AI must first analyze the user's question to determine if it pertains to an individual. If it does, the AI is*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested the addition of functionality to incorporate runtime data from Human through the Command Line Interface (CLI). This enhancement allows for dynamic data input from the Human interface directly into the system during its operation. Furthermore, there are plans to expand this functionality by implementing WebSockets. The integration*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case to address issue #2260. This addition aims to enhance the validation process, specifically targeting scenarios related to checking if the "get_new_copy" function duplicates data as intended. The proposed test case will further improve the correctness and reliability of the function by ensuring it*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2448, focusing on streamlining user memory configuration. The original code checked for both `self.memory_config` and `user_memory` within it. The proposed solution simplifies this by primarily verifying the presence of `memory_config`. The updated logic directly initializes `self._user_memory` with a `UserMemory` instance, utilizing the crew*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when tools are used within a crew via the `crewai run` command. This process inadvertently creates a virtual environment that identifies `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes that `crewai_tools` should be installed universally, irrespective of whether*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the existing work done in pull request #2422. The suggestion focuses on refining and improving the current implementation by addressing certain identified issues. Furthermore, the suggestion includes the removal of a specific test case that was deemed unnecessary or redundant for the overall functionality and*

## ⭐ Starred Repositories
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
