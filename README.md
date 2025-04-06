# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that when initializing the MDXSearchTool, it is necessary to pass a `config` parameter. The configuration should be a dictionary specifying the language model (LLM) and embedder. The LLM configuration includes the provider (e.g., "ollama") and its specific settings like the model name. Similarly, the embedder configuration specifies*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the codebase by implementing more robust and informative error handling mechanisms. This includes providing more descriptive error messages, potentially using error codes, and implementing comprehensive logging for debugging purposes. The aim is to improve the developer experience, streamline debugging, and provide clearer insights into potential issues*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested initializing all language models (LLMs). However, to optimize, one could initialize a single LLM and assign it to others, which should function effectively. Regarding the selection of OpenAI as the default LLM, Vidit-Ostwal suggests it gained prominence due to its early adoption and widespread use. Similar to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested defining a custom LLM and using the `llm` parameter within the CrewAI framework. This approach allows users to specify their preferred language model for agent operations. To implement this, you can instantiate an `LLM` object, configuring parameters like the model name, for example, "gemini/gemini-1.5-pro-latest," and temperature. The*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested a follow-up regarding a previously discussed solution. The suggestion seeks confirmation on whether the implemented solution was effective and successful for the intended user. The query aims to ascertain if the proposed approach resolved the initial problem or addressed the specific need. The intention is to validate*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested upgrading the version to potentially resolve an issue. This recommendation is based on the assumption that the current problem might stem from using an outdated version. Upgrading could incorporate bug fixes, performance improvements, or compatibility enhancements that address the existing problem. It is advised to test the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested a solution to address a prompt engineering problem, hypothesizing that providing the large language model (LLM) with more information about the tool might resolve the issue. The suggested solution involves replacing a specific function within the `base_tool.py` file, with a modified function that generates a more detailed*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being utilized. This inquiry stems from an apparent discrepancy observed when comparing the LLM in question to Gemini. According to @Vidit-Ostwal, when testing with Gemini, the reported issue did not arise, indicating a potential difference in behavior or configuration*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested investigating how to view the prompt sent to the language model (LLM), noting that using verbose mode does not provide sufficient information. They specifically mention the inability to directly see the `final_prompt` before it's passed to the LLM. To address this, they implemented a temporary solution by*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a prompt for an AI People Information Specialist. The AI should analyze user questions, use available tools to search for information about individuals, and provide a concise summary of findings. The AI's goal is to answer questions about people using specified tools. It will use the "Search*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested an enhancement to the CLI tool by incorporating the ability to add runtime data sourced from Human. The initial implementation focuses on providing this capability directly through the command-line interface. Future development plans involve expanding this functionality to include support for websockets. This addition aims to facilitate*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case to address issue #2260. This new test is designed to verify the correct behavior of the system in handling a specific scenario related to the identified problem. The test aims to ensure that a particular action or process functions as expected and to*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested improvements for initializing `user_memory`. The initial code checked for both `self.memory_config` and `user_memory` within it, which was deemed inefficient. The new logic directly checks for `self.memory_config`. The code initializes `self._user_memory` with that instance if `user_memory` is a valid `UserMemory` instance. Otherwise, `self._user_memory` is initialized with `UserMemory(crew=self)`. Consequently,*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when tools are used within a crew via the `crewai run` command. This process inadvertently creates a virtual environment that treats `crewai_tools` as an optional dependency. To address this, Vidit-Ostwal proposes ensuring that `crewai_tools` is installed universally, irrespective of whether*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the changes introduced in pull request #2422. The comment indicates a continuation of work related to that specific pull request, implying further refinements or additions to the existing codebase. Specifically, the suggestion involves the removal of a test case that was deemed unnecessary or redundant.*

## ⭐ Starred Repositories
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
