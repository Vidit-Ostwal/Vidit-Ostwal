# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that when initializing the `MDXSearchTool`, a `config` parameter needs to be passed. This configuration should be a dictionary containing settings for both the language model (`llm`) and the embedding model (`embedder`). The language model configuration includes the provider (e.g., "ollama") and specific model settings like the model*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested that the current implementation for handling asynchronous operations can be improved by utilizing a more efficient approach. The focus should be on reducing overhead and optimizing resource utilization. This improvement aims to make the process more streamlined and responsive, therefore improving overall performance and providing faster execution*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested initializing each language model (LLM), noting that initializing one and assigning the others to it could work. They explained that OpenAI's API became the default due to its early adoption and widespread use. Other companies made their APIs compatible with OpenAI's for simpler integration, acting as a*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested that users can define their own Language Model and integrate it into the crew using the 'llm' parameter. This approach allows for customization and flexibility in selecting the desired LLM for specific tasks. The provided code snippet demonstrates how to define an LLM, specifying parameters such as*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested following up on a previous interaction. The comment inquires whether a prior suggestion or solution was successful for the intended recipient. The comment serves as a check-in to determine if the user encountered any issues or achieved the desired outcome following the implementation of earlier advice. Furthermore,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested addressing a potential issue by upgrading to a newer version and then re-evaluating the situation. The suggestion is aimed at resolving an unspecified problem or improving the current functionality. The core idea is to implement an update. After upgrading the version, the user should try again to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested that the issue might stem from prompt engineering. To address this, they propose enhancing the information provided to the language model about the tool. A potential solution involves modifying a specific function related to generating descriptions. The suggested modification aims to provide more context on the functionality*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific language model being utilized, referencing a previous comment. They indicated having tested a similar scenario using Gemini, where the observed issue was not apparent. This suggests a potential difference in behavior or outcome depending on the language model in use. The intention is*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a way to view the prompt sent to the language model (LLM). They noted that using verbose mode doesn't provide sufficient information to see the final prompt. To address this, Vidit-Ostwal implemented a solution by adding a print statement. This print statement specifically targets the list of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested that the prompt sets up an AI assistant designed to find information about people. The system message defines the AI's role as a "People Information Specialist" with the goal of analyzing questions, using tools to search for individuals, and providing concise findings. The AI is restricted to*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: @Vidit-Ostwal has suggested implementing a feature to incorporate runtime data from Human through the Command Line Interface (CLI). This enhancement aims to provide a more dynamic and interactive way to integrate Human data. The initial implementation focuses on enabling data input via the CLI. Future development plans involve expanding the*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case to address issue #2260. This addition aims to improve the overall test coverage and robustness of the system. The inclusion of this new test case should help validate the fix implemented for the aforementioned issue. By introducing this test, the project aims to*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2448, detailing key logic changes related to user memory configuration within the Crew class. The prior code checked for both `self.memory_config` and `user_memory` in `memory_config`. The proposed logic simplifies this by verifying `memory_config`'s presence. It initializes `self._user_memory` with a `UserMemory` instance if provided*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when tools are used within a crew via the `crewai run` CLI command. This process creates a virtual environment that treats `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes ensuring that `crewai_tools` is installed irrespective of whether any*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the foundation established in issue #2422. The focus is on refining the existing work by streamlining the test suite. Specifically, this involves removing a test case deemed unnecessary or redundant. The intention is to improve the overall efficiency and clarity of the testing process. By*

## ⭐ Starred Repositories
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
