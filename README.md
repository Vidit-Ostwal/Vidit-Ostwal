# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/2652#issuecomment-2818063996) in [crewAIInc/crewAI] on 2025-04-21.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the process for addressing suggestions or questions within the current workflow. They are seeking a more structured approach to manage and track individual points raised, aiming for improved organization and clarity. Instead of ad-hoc discussions, they propose formally documenting each point as a separate, trackable item.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2652#issuecomment-2817812953) in [crewAIInc/crewAI] on 2025-04-21.
  > *AI Summary: @Vidit-Ostwal has suggested that CrewAI is currently supported with Python versions 3.10, 3.11, and 3.12. The test cases also confirm that the framework is being tested for Python 3.10 compatibility. To address any potential issues, @Vidit-Ostwal requested more information about the specific problem being experienced. Providing details regarding the exact*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2522#issuecomment-2817605942) in [crewAIInc/crewAI] on 2025-04-21.
  > *AI Summary: Vidit-Ostwal has suggested a potential issue with CrewAI's dependency on LiteLLM. They've raised a concern about pinning LiteLLM to a specific version. If LiteLLM isn't version-locked, installing CrewAI might lead to the installation of the newest LiteLLM version, which they claim releases stable versions frequently. This rapid release cycle of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2650#issuecomment-2817193005) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested seeking an example to better understand the intended usage of certain objects. The objects in question are broadly categorized into three types. First, are container types like Lists, Dictionaries, and Sets. Second, are standard objects like datetime and time. Third, encompasses custom objects, exemplified by "MyCustomObject." A*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2632#issuecomment-2817190941) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested an alternative approach to address the issue of running CrewAI asynchronously with multiple inputs. Based on examination of the existing code, they believe the `kickoff_for_each_async()` function within CrewAI could provide a solution. This function is specifically designed to handle asynchronous execution with multiple inputs. Vidit-Ostwal recommends testing*
- [Commented](https://github.com/crewAIInc/crewAI/issues/718#issuecomment-2817075569) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested a potential quick bypass solution, though its feasibility is uncertain. The idea revolves around hosting the model on Hugging Face and subsequently utilizing Hugging Face as the provider. Vidit-Ostwal acknowledges that this approach might offer a temporary workaround. While suggesting this possible bypass, Vidit-Ostwal mentions a commitment*
- [Commented](https://github.com/crewAIInc/crewAI/issues/718#issuecomment-2817075062) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue stems from how CrewAI handles custom embeddings when an embedder is provided within the crew. CrewAI has its method for managing this. Currently, the tools being used rely on Embedchain to empower the RAG tool. Embedchain's list of providers doesn't seem to support custom*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2642#issuecomment-2817037446) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested that the proposed solution should ideally be effective. In their opinion, the approach under consideration is likely to yield the desired results. They believe that the methodology aligns well with the objectives and should produce a successful outcome. While acknowledging the potential for unforeseen challenges, they express*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2647#issuecomment-2817035431) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested seeking clarification regarding the configuration of the `planning_llm` when it resolves an issue. The suggestion includes defining the `planning_llm` using an LLM with specific parameters like model name, temperature, base URL, and API key. Vidit-Ostwal has also suggested confirming whether the defined LLM is compatible with Litellm*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2645#issuecomment-2817032826) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the usage of the LLM class within CrewAI, emphasizing its intended application within the crew context. Referencing the official documentation, they highlight the importance of utilizing CrewAI's built-in LLM class, especially when integrating with a crew setup. Furthermore, Vidit-Ostwal raises a critical point regarding validation, proposing*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2616) in [crewAIInc/crewAI]: [BUG] Broken Test Case (2025-04-16).
  > *AI Summary: @Vidit-Ostwal has suggested that there is a broken test case related to Mem0 storage, specifically in the `test_mem0_storage.py` file. The error arises during the setup of `test_mem0_storage_with_explict_config`, stemming from an `OpenAIError` that indicates the absence of an OpenAI API key, either passed directly or set as an environment variable. The*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2610) in [crewAIInc/crewAI]: Branch 2379 (2025-04-15).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2379. The proposed resolution addresses an identified problem, aiming to rectify the reported behavior or defect. The fix is intended to resolve the underlying cause of the issue. By implementing this correction, the goal is to eliminate the occurrence of the previously reported*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2580) in [crewAIInc/crewAI]: Fix Mistral Issue: (2025-04-10).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2571. The proposed solution addresses the problem described in the mentioned issue. The suggested fix aims to resolve the underlying cause of the problem. It intends to correct the behavior and ensure the system operates as expected. The contribution offers a direct remedy*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2570) in [crewAIInc/crewAI]: added condition to check whether _run function returns a coroutine ob… (2025-04-10).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue number 2538. The proposed solution addresses a problem identified in the existing codebase. The suggested modifications aim to resolve the reported problem and improve the overall functionality or stability of the software. The issue was pinpointed and is now directly targeted by this*
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested adding functionality to incorporate runtime data from Human through the Command Line Interface. The proposed enhancement focuses on enabling the system to receive and process real-time information originating from Human via the CLI. This addition aims to improve the system's capabilities by allowing it to dynamically adapt*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case that addresses issue #2260. The test aims to verify the correct behavior of a specific function when handling edge cases or unusual inputs. The test case will ensure that the function behaves as expected, contributing to the overall robustness and reliability of the*

## ⭐ Starred Repositories
- Starred [google/A2A](https://github.com/google/A2A) on 2025-04-18.
- Starred [google/A2A](https://github.com/google/A2A) on 2025-04-15.
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.

## 🍴 Forked Repositories
- Forked [google/A2A](https://github.com/Vidit-Ostwal/A2A) on 2025-04-21.
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
