# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that when initializing the `MDXSearchTool`, it is necessary to pass a `config` parameter. This configuration should be a dictionary that specifies settings for both the language model (`llm`) and the embedder. The language model configuration includes the provider (such as "ollama") and its specific settings like the*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested improvements to the contribution guidelines, emphasizing the importance of clear and concise instructions for new contributors. The suggestion involves streamlining the process of setting up the development environment, clarifying code style and formatting requirements, and ensuring the documentation is accurate and up-to-date. The proposal aims to make*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested that initializing each language model (LLM) might be necessary, but a shortcut could involve initializing one LLM and assigning it to the others. Addressing the query regarding OpenAI as the default LLM, Vidit-Ostwal suggests its early adoption and wide compatibility led to its selection. Companies aligning their*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested that users can define their own Large Language Models (LLMs) and incorporate them into the crew setup using the 'llm' parameter. This allows for customization and flexibility in choosing the desired LLM for specific tasks within the crew. An example of how to set up and integrate*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested following up on a previous interaction. The suggestion inquires about the success of a prior recommendation or solution offered to another user. The aim is to determine if the assistance provided was effective in resolving the user's issue or achieving the desired outcome. The comment seeks confirmation*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested a potential solution to an issue that might be arising. To address the problem effectively, Vidit-Ostwal has recommended taking a specific course of action which is to upgrade the current version of the software or system being used. Following the upgrade, it's advisable to retry the operation*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the problem lies in prompt engineering and believes providing the LLM with more information about the tool might resolve it. They propose a solution involving replacing a specific function. This function enhances the description by detailing its operation, arguments, and usage, aiming to improve the LLM's*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being utilized. Experiencing no issues when implementing Gemini, @Vidit-Ostwal proposes the query to isolate discrepancies. By identifying the LLM in use, a comparative analysis can be conducted to ascertain potential variations in performance or behavior. This information could prove*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested that the current verbose setting does not provide sufficient information to view the final prompt sent to the language model (LLM). To address this, Vidit-Ostwal proposes a method to access the prompt. They added a print statement within the `crew_agent_executor.py` file, specifically just before the LLM call.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a prompt for an AI assistant designed as a People Information Specialist. This assistant should analyze user questions, focusing on identifying if the query pertains to a specific person. If so, the assistant will leverage a tool, "Search a JSON's content," to find information within a predefined*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested the addition of functionality that enables the incorporation of runtime data originating from Human through the command-line interface (CLI). This enhancement allows users to dynamically integrate data from Human during program execution. The proposed functionality will be further expanded upon by the integration of WebSocket technology. This*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case related to issue #2260. The goal of this test case is to verify the correct behavior of the system when a specific scenario occurs, ensuring that the relevant functionality operates as expected. The test case aims to confirm that when a certain action*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2448 by modifying the logic for initializing `self._user_memory`. The original code checked for both `self.memory_config` and `user_memory` within it, which Vidit-Ostwal deems inefficient. The revised logic simplifies this by only checking for `self.memory_config`. If `user_memory` is a valid instance of `UserMemory`, it's directly*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, addressing a problem encountered when using tools within a crew via the `crewai run` command. The process of creating a virtual environment incorrectly identifies `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes that `crewai_tools` should be consistently installed, irrespective of*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the existing work in pull request #2422. The focus of this update is to refine the current implementation by removing an unnecessary test case. This change aims to streamline the testing process and reduce redundancy within the test suite. The removal of this specific test*

## ⭐ Starred Repositories
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
