# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2770437182) in [crewAIInc/crewAI] on 2025-04-01.
  > *AI Summary: Vidit-Ostwal has suggested offering assistance by attempting to reproduce a specific issue, expressing a willingness to investigate the problem further. The suggestion involves a request for the code, implying a desire to examine the code and identify the root cause of the issue. This approach aims to facilitate a deeper*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2508#issuecomment-2770385814) in [crewAIInc/crewAI] on 2025-04-01.
  > *AI Summary: Vidit-Ostwal has suggested employing prompt engineering to address the issue. The suggested approach involves instructing the agent to incorporate an input, specifically a `search_query`, when utilizing the designated tool. This method aims to guide the agent in formulating queries more effectively, leading to improved search results and more relevant outputs.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2487#issuecomment-2766352971) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: Vidit-Ostwal has suggested clarifying how the user input is being obtained, questioning if 'human_input' is being utilized. The response clarifies that 'human_input' is not being used. Instead, the questions are sent via WebSocket, and the system waits for the user's reply. This approach is part of a custom tool that*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2487#issuecomment-2766341623) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the method used to obtain user input. The suggestion emphasizes understanding the precise approach implemented for acquiring input data, particularly questioning whether the 'human_input' function or a similar mechanism is being utilized. The focus is on gaining clarity regarding the input acquisition process. The suggestion underscores*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2487#issuecomment-2766336429) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: Vidit-Ostwal has suggested an alternative approach to troubleshooting the crew setup. The suggestion involves running the crew setup directly within a Jupyter Notebook environment. Additionally, they propose attempting to execute the setup using a standalone Python script, identified as "python.py." The intent is to bypass any potential complications arising from*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2487#issuecomment-2766310282) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: @Vidit-Ostwal has suggested that the author share details about the project under development. The suggestion emphasizes a desire to understand the project's goals and implementation. A key aspect of the request is access to the source code, which would allow for a deeper comprehension of the project's architecture and functionality.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2227#issuecomment-2766251238) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: @Vidit-Ostwal has suggested checking if a specific issue has been resolved in the latest version. The suggestion is based on an observation made while creating a new project using the `crewai create crew Project-name` command. The author mentions that all Ruff checks passed during this process. This indicates a potential*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2500#issuecomment-2766186099) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: Vidit-Ostwal has suggested gathering more logs to aid in troubleshooting. They attempted to replicate the reported issue by installing crewai in a fresh environment and creating a project using the specified command, which executed without problems. To further investigate the issue, Vidit-Ostwal proposes that the user experiencing the problem provide*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2487#issuecomment-2766000094) in [crewAIInc/crewAI] on 2025-03-31.
  > *AI Summary: @Vidit-Ostwal has suggested that the reason for the issue likely stems from the use of a `try-except` block within the `crew-ai` library. This block is implemented because the library has a built-in functionality to make multiple attempts to achieve the agent's objectives. The `try-except` structure is employed to handle potential*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2307#issuecomment-2764720493) in [crewAIInc/crewAI] on 2025-03-30.
  > *AI Summary: Vidit-Ostwal has suggested that the pull request is still a work in progress. Despite uncertainty about its current functionality, Vidit-Ostwal assures that the issues will be resolved shortly. The user expresses gratitude for the notification and acknowledges the importance of addressing the raised concerns. The comment also makes a reference*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: @Vidit-Ostwal has suggested adding a new functionality to incorporate runtime data from Human through the Command Line Interface. The goal is to enable users to input and manage data originating from the Human system directly via CLI commands, thus streamlining the integration process. The proposed enhancement aims to create a*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: @Vidit-Ostwal has suggested adding a test case to address issue #2260. This addition aims to enhance the project's testing suite and provide more robust coverage. The test case is intended to validate specific functionality or behavior related to the identified issue. By incorporating this test, the project can better ensure*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested changes to fix issue #2448 regarding user memory configuration. The prior code checked for both `self.memory_config` and `user_memory` within it. The revised logic simplifies this by directly checking `self.memory_config`. If `user_memory` is present and is a `UserMemory` instance, it's used directly. Otherwise, `self._user_memory` is initialized with a*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, addressing a problem encountered when using tools within a crew via the `crewai run` CLI command. The core issue arises because the virtual environment created during this process mistakenly treats `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes that `crewai_tools`*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2423) in [crewAIInc/crewAI]: Changed the import error to show missing module files (2025-03-20).
  > *AI Summary: @Vidit-Ostwal has suggested building upon the existing work in pull request #2422. The comment indicates a continuation of efforts related to a previous submission. The focus is on refining and improving the current state of the code. It also states that an unneeded test case has been removed. This modification*

## ⭐ Starred Repositories
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
