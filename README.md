# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2780728915) in [crewAIInc/crewAI] on 2025-04-05.
  > *AI Summary: Vidit-Ostwal has suggested that when initializing the `MDXSearchTool`, a `config` parameter should be passed. This configuration should be a dictionary containing specifications for both the language model (llm) and the embedder. The llm configuration should include the provider (such as "ollama") and its specific settings, like the model name ("llama2").*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2024#issuecomment-2779235679) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: @Vidit-Ostwal has suggested a streamlined process for managing prompt engineering workflows, highlighting the iterative nature of prompt creation and improvement. They emphasize the importance of tracking prompt versions, input data, model parameters, and resulting outputs. The proposal advocates for a system that allows easy comparison between different prompt versions, facilitating*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2779055100) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested initializing each language model (LLM). As a helpful tip, initializing one LLM and assigning it to others should work effectively. Addressing the choice of OpenAI as the default LLM, Vidit-Ostwal explains that its API gained prominence due to early adoption and widespread use. This compatibility simplifies integration*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2517#issuecomment-2778410185) in [crewAIInc/crewAI] on 2025-04-04.
  > *AI Summary: Vidit-Ostwal has suggested that users can define their own Large Language Models (LLMs) and integrate them into the crew setup via the `llm` parameter. This allows for flexibility in choosing and configuring the specific LLM used within the crew. The suggestion emphasizes the ability to customize the LLM to suit*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2288#issuecomment-2776559533) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested following up on a previous interaction. The suggestion is a direct inquiry about the success of a prior recommendation or solution. It shows engagement and a desire to ensure the provided advice was helpful and effective for the recipient. This indicates a proactive approach to problem-solving and*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2101#issuecomment-2776553749) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: @Vidit-Ostwal has suggested a potential solution to an issue. The suggestion involves upgrading to a newer version and then reattempting the previous action. This approach aims to resolve the problem by incorporating the latest updates and improvements. The underlying principle is that the newer version might contain fixes or enhancements*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2776524457) in [crewAIInc/crewAI] on 2025-04-03.
  > *AI Summary: Vidit-Ostwal has suggested addressing a prompt engineering problem by providing the language model with more information about the tool. As a potential solution, they've proposed replacing a specific function within the `base_tool.py` file. The suggested function focuses on generating a detailed description of the tool, outlining its usage instructions, required*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773146947) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: @Vidit-Ostwal has suggested inquiring about the specific large language model (LLM) being used. They indicated that when testing a similar scenario with Gemini, they did not encounter the issue being discussed. Therefore, understanding which LLM is in use could help in identifying the root cause of the problem. Gathering this*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773137518) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a method to view the final prompt sent to the language model (LLM). Noting that the verbose setting doesn't provide sufficient information, they highlight the difficulty in accessing the complete prompt. To address this, they implemented a print statement within the `crew_agent_executor.py` file, specifically before the LLM*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2773121476) in [crewAIInc/crewAI] on 2025-04-02.
  > *AI Summary: Vidit-Ostwal has suggested a system for an AI assistant designed to be a People Information Specialist. The AI's primary function is to analyze user questions, determine if they pertain to a person, and use available tools to find relevant information. It should summarize the findings concisely in a single paragraph.*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested adding a new feature that allows users to incorporate runtime data originating from human input through the Command Line Interface (CLI). The implementation focuses on enabling the system to receive and process real-time data entered by users, improving the interactive capabilities of the application. Vidit-Ostwal has also*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case to address issue #2260. The test aims to verify the behavior of the "add user to group" functionality in a scenario where the user is already part of another group with the same scope. The test case will confirm that the user is*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2448, focusing on simplifying the user memory configuration within the Crew class. The original logic checked for both `self.memory_config` and `user_memory` within it. @Vidit-Ostwal proposes streamlining this by directly verifying if `memory_config` is present with "mem0" as the provider. The updated logic initializes*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, addressing a problem encountered when using tools within a crew via the `crewai run` CLI command. The core issue arises because the virtual environment created by this command treats `crewai_tools` as an optional dependency, leading to potential problems. Vidit-Ostwal proposes that `crewai_tools`*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: Vidit-Ostwal has suggested building upon the existing work in pull request #2422. The suggestion focuses on refining the current implementation by removing a specific test case that is deemed unnecessary. This change aims to streamline the testing process and improve the overall efficiency of the codebase. The removal of the*

## ⭐ Starred Repositories
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
