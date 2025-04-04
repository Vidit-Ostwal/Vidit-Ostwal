# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested that users have the flexibility to define their own Large Language Models (LLMs) and incorporate them into the crew using the `llm` parameter. This allows for customization and integration of specific LLMs according to user preferences or requirements. The provided code snippet demonstrates how to define an*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested following up on a previous interaction. The suggestion inquires whether a prior solution or recommendation was effective for the intended recipient. The commenter is seeking confirmation or feedback regarding the implementation or outcome of the advice given. Essentially, it's a check-in to determine if the assistance provided*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested a potential solution involving a version upgrade. The suggestion is directed towards resolving an unspecified issue encountered by another user. While the specific context of the problem and the target software or library remain undefined, the core recommendation centers around the possibility that an outdated version might*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested a solution related to prompt engineering to address an issue, hypothesizing that providing the language model with more information about the tool might resolve it. They propose replacing a specific function in the base_tool.py file with a modified version. The suggested function aims to give more information*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being utilized. They mentioned that they attempted the same task with Gemini and did not encounter a similar issue. Therefore, understanding which LLM is in use might provide insight into the discrepancy and help identify the root cause of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a method to view the final prompt sent to the LLM, noting that using verbose mode doesn't provide sufficient information. They observed the lack of direct access to the `final_prompt` before the LLM call. To address this, they implemented a solution by printing the list of messages*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a system message for an AI assistant designed to be a People Information Specialist. The assistant's primary function is to find and summarize information about individuals using a specific tool that searches a JSON file. The assistant should analyze user questions, determine if they pertain to a*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2772748349) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the current implementation may be fragile. The primary concern revolves around the potential for the language model to return a different nested dictionary structure with varying keys in the future. This could lead to the failure of the current system, which appears to be reliant on*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2772740950) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested that the current pull request removes necessary validations performed by crewAI by permitting a dictionary-like structure. While this resolves the immediate problem, Vidit-Ostwal believes there are superior long-term solutions. As the number of tools increases, the language model should intelligently determine necessary parameters by learning function details*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2772555576) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested that while the solution works, a more streamlined approach should allow tasks to pass consistent outputs, like JSON or Pydantic models, as inputs to other tasks. They propose integrating this functionality into the `tasks.yaml` templates. Vidit-Ostwal believes the current design incorporates all information into the LLM's working*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested enhancing the CLI tool to incorporate runtime data sourced from Human. This addition broadens the tool's capabilities, enabling it to process and integrate real-time information. The proposed functionality aims to improve the tool's efficiency and responsiveness. The next phase involves expanding the implemented features by incorporating WebSocket*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case related to issue #2260. This addition aims to comprehensively test the functionality and ensure its proper behavior. This new test case is designed to cover various scenarios and edge cases associated with the referenced issue. By incorporating this test, the project can better*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix related to user memory configuration. The original code checked for both `memory_config` and `user_memory` and could be more efficient by verifying the `provider`. The suggestion removes the need to check if `user_memory_config` is a dictionary. Instead of raising a TypeError, the suggested code initializes `self._user_memory`*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, addressing a problem encountered when using tools within a crew via the `crewai run` command. The process creates a virtual environment and mistakenly considers `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes ensuring that `crewai_tools` is installed irrespective of whether*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: Vidit-Ostwal has suggested a refinement based on a previous issue, specifically building upon the work done in issue #2422. The primary focus of the contribution is to streamline the existing codebase. This was achieved by eliminating a particular test case that was deemed unnecessary. The rationale behind this change is*

## ⭐ Starred Repositories
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
