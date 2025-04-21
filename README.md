# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2650#issuecomment-2817193005) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested providing an example to better understand the context in which certain elements are being utilized. They express interest in learning the specific scenarios where these elements are applied. The comment lists several categories of objects, including containers like lists, dictionaries, and sets, as well as standard objects*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2632#issuecomment-2817190941) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested an alternative approach for running CrewAI asynchronously with multiple inputs, based on their understanding of the code. They propose utilizing the `kickoff_for_each_async()` method, which CrewAI provides as a specific way to handle such scenarios. They believe this method could potentially resolve the issue at hand. To determine*
- [Commented](https://github.com/crewAIInc/crewAI/issues/718#issuecomment-2817075569) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested a potential quick bypass. The suggestion involves hosting the model on Hugging Face and utilizing Hugging Face as the provider. The idea is proposed as a temporary fix. The feasibility of this approach isn't certain, and Vidit-Ostwal is unsure whether it will be effective. While considering this*
- [Commented](https://github.com/crewAIInc/crewAI/issues/718#issuecomment-2817075062) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the problem arises from how CrewAI manages custom embeddings when an embedder is provided within the crew. CrewAI's internal handling of embeddings differs from the approach used with tools. Specifically, the RAG tool relies on Embedchain, which currently does not support custom models. This lack of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2642#issuecomment-2817037446) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested that a proposed solution should ideally be effective. The assessment is based on their evaluation of the approach's suitability and expected performance. Their comment conveys a positive outlook regarding the outcome, indicating an expectation that the solution will function as intended. This suggestion implies a level of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2647#issuecomment-2817035431) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested seeking clarification regarding the configuration of the `planning_llm` that resolves a reported issue. They provided a code snippet illustrating how the LLM might be set up, specifying the model, temperature, base URL, and API key. Furthermore, Vidit-Ostwal inquired about the compatibility of the defined LLM with Litellm,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2645#issuecomment-2817032826) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested that the LLM class provided by CrewAI should be used when working with a crew. They recommend reviewing the CrewAI documentation for LLMs. This suggestion brings up a potential issue regarding validation. When an agent and crew are defined, there should be a validation check to ensure*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2421#issuecomment-2816831311) in [crewAIInc/crewAI] on 2025-04-19.
  > *AI Summary: @Vidit-Ostwal has suggested that a merge should occur. This suggestion indicates a desire to incorporate changes or updates into a primary codebase or project. The implication is that the proposed changes are ready for integration and would benefit the overall project. The user likely believes that the current state of*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2307#issuecomment-2816829318) in [crewAIInc/crewAI] on 2025-04-19.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might stem from ChromaDB's dimension locking. When a collection is initially created, it accepts vectors of any dimensionality. However, after the first embeddings are added, the collection locks to that specific dimensionality. This requires consistent use of the same embedding function for all subsequent*
- [Commented](https://github.com/mindverse/Second-Me/issues/157#issuecomment-2816816529) in [mindverse/Second-Me] on 2025-04-19.
  > *AI Summary: Vidit-Ostwal has suggested clarifying whether resetting the memory addresses the current issue. The inquiry focuses on determining the appropriate course of action to resolve a problem. Vidit-Ostwal is considering two potential solutions: resetting the memory or deleting the data folder and restarting from scratch. The goal is to understand which*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2616) in [crewAIInc/crewAI]: [BUG] Broken Test Case (2025-04-16).
  > *AI Summary: @Vidit-Ostwal has suggested there's a broken test case related to Mem0 storage, specifically in the `test_mem0_storage.py` file. The test failure occurs during the setup of `test_mem0_storage_with_explict_config`. The error stems from the OpenAI client initialization, which requires an API key to be set either directly or via the `OPENAI_API_KEY` environment variable.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2610) in [crewAIInc/crewAI]: Branch 2379 (2025-04-15).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue number 2379. The suggested solution addresses a problem that has been identified and tracked under this specific issue number. The proposed change aims to resolve the underlying cause of the issue, leading to a more stable and reliable system. This update is designed*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2580) in [crewAIInc/crewAI]: Fix Mistral Issue: (2025-04-10).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2571. The fix addresses the problem outlined in the issue description. The solution focuses on resolving the reported behavior. The implementation improves upon the existing code by incorporating the suggested changes. This approach involves modifying the current logic to align with the expected*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2570) in [crewAIInc/crewAI]: added condition to check whether _run function returns a coroutine ob… (2025-04-10).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue number 2538. This contribution aims to address and resolve the problems outlined in the aforementioned issue. By implementing this fix, the goal is to improve the overall stability and functionality of the system. The proposed solution is designed to directly tackle the root*
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: Vidit-Ostwal has suggested adding a feature to input runtime data from Human using the Command Line Interface (CLI). This enhancement aims to streamline data input and processing. Further development will involve incorporating websockets to expand the functionality. The inclusion of websockets will likely facilitate real-time data transmission and interaction with*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: @Vidit-Ostwal has suggested adding a test case to address issue #2260. The suggested test aims to verify a scenario involving specific data structures and potential edge cases. The test is designed to ensure the robustness and correctness of the related functionality. It focuses on preventing regressions and maintaining the integrity*

## ⭐ Starred Repositories
- Starred [google/A2A](https://github.com/google/A2A) on 2025-04-18.
- Starred [google/A2A](https://github.com/google/A2A) on 2025-04-15.
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
