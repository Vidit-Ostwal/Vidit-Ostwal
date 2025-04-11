# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2575#issuecomment-2794502131) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: @Vidit-Ostwal has suggested the issue primarily affects CI jobs using Python 3.10, as jobs on Python 3.11 and 3.12 are unaffected. The problem stems from incompatibility with `from typing import Self` in Python 3.10. Additionally, they recommended yanking version 0.114.0 after the new release to prevent Python 3.10 users from*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2575#issuecomment-2794466731) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: Vidit-Ostwal has suggested that the reported issue appears widespread, affecting CI jobs that install CrewAI without version pinning, causing them to fail. He proposes releasing a new version soon to resolve this problem. He identifies the failure stems from the absence of a version lock on the CrewAI install. This*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2575#issuecomment-2794453606) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: Vidit-Ostwal has suggested that the identified issue has been successfully addressed and a fix has been implemented. The upcoming version of the software or system is expected to include this fix, resolving the previously reported problem. This update will likely improve the overall functionality and address any concerns raised regarding*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2574#issuecomment-2794399222) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: Vidit-Ostwal has suggested investigating the intermittent behavior reported by the user. To understand the issue better, Vidit-Ostwal requests the complete CLI logs for both successful and unsuccessful scenarios. Furthermore, they advise enabling verbose logging for both the crew and the agent. Analyzing these logs should provide valuable insights into the*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2570#issuecomment-2794102458) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2434. The proposed solution addresses the problem described in the aforementioned issue, aiming to resolve the reported bug or enhancement request. The fix presumably involves modifications to the codebase. These changes aim to improve the functionality, stability, or performance related to the specific*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2545#issuecomment-2792908946) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: @Vidit-Ostwal has suggested closing the current issue. After a period of discussion and contributions aimed at resolving the initial problem, it seems a consensus has been reached, indicating the completion of the objectives associated with the issue. Considering the issue's resolution and the implied agreement among participants, closing it would*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2549#issuecomment-2792815047) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the user share their entire crew setup.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2563#issuecomment-2791921224) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: Vidit-Ostwal has suggested updating the CrewAI version, indicating a potential resolution to a previously discussed issue. The suggestion implies a fix or enhancement related to the current CrewAI version that addresses a specific problem. By upgrading, HarikrishnanK9 can benefit from the updates. It's important to ensure that the update is*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2545#issuecomment-2791514384) in [crewAIInc/crewAI] on 2025-04-10.
  > *AI Summary: Vidit-Ostwal has suggested that the configuration of the `input_dict` is causing the reported problem. When `inputs` is set, the code tries to find a key inside `input_dict`. Vidit-Ostwal proposed a way to configure the dictionary to resolve this issue. Furthermore, Vidit-Ostwal inquired about adding a functionality to the `interpolate_inputs_and_add_conversation_history` function*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2434#issuecomment-2790819491) in [crewAIInc/crewAI] on 2025-04-09.
  > *AI Summary: Vidit-Ostwal has suggested that the `_run` method, defined as abstract and asynchronous within the `snowflake_tool`, is called by a synchronous `run` method in the base tool class. This discrepancy, in Vidit-Ostwal's view, may be the underlying cause of improper awaiting behavior. They have identified this issue as the reason for*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2570) in [crewAIInc/crewAI]: added condition to check whether _run function returns a coroutine ob… (2025-04-10).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue number 2538. The provided solution addresses the reported problem, aiming to resolve the underlying cause and improve the overall functionality. The implemented changes directly target the root of the issue, ensuring a comprehensive and effective resolution. The suggested fix has been thoroughly tested*
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested adding a new functionality to the Command Line Interface (CLI) that allows users to incorporate runtime data sourced from Human. The primary goal of this addition is to enhance the CLI's data handling capabilities by enabling it to directly receive and process real-time information. Furthermore, there are*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case addressing issue #2260. The addition aims to verify the correct functioning of a particular feature or fix. This test case is designed to ensure that the system behaves as expected under specific conditions. The goal is to improve the overall robustness and reliability*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2469) in [crewAIInc/crewAI]: Fixes user_memory configuration (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2448, focusing on streamlining the user memory configuration for the Crew class. The existing logic involved multiple checks for 'memory_config' and 'user_memory', which Vidit-Ostwal proposes simplifying. Instead of verifying if 'user_memory_config' is a dictionary, the revised code directly initializes self._user_memory with UserMemory, passing*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2468) in [crewAIInc/crewAI]: Crewai_tools is an absolute dependency (2025-03-25).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2361, which arises when using tools within a crew with the `crewai run` CLI command. This process creates a virtual environment that mistakenly considers `crewai_tools` as an optional dependency. To resolve this, Vidit-Ostwal proposes that `crewai_tools` should be installed as a standard dependency.*

## ⭐ Starred Repositories
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.
- Starred [karpathy/LLM101n](https://github.com/karpathy/LLM101n) on 2025-03-16.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
