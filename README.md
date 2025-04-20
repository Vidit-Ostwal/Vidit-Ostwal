# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2650#issuecomment-2817193005) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested the need for an example to better understand the intended use case. To illustrate possible applications, Vidit-Ostwal has presented a categorized list of object types. This list is divided into three categories. The first category includes standard Python containers such as Lists, Dictionaries, and Sets. The second*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2632#issuecomment-2817190941) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested an alternative approach to address the issue of running CrewAI asynchronously with multiple inputs. Based on the code, the user seems to be attempting to execute CrewAI in an asynchronous manner with several inputs. Vidit-Ostwal recommends exploring the `kickoff_for_each_async()` method provided by CrewAI, believing it could offer*
- [Commented](https://github.com/crewAIInc/crewAI/issues/718#issuecomment-2817075569) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested a potential quick bypass. The idea involves hosting the model on Hugging Face and utilizing Hugging Face as the provider. This approach might offer a temporary workaround to address existing issues. While acknowledging uncertainty regarding the feasibility of this method, Vidit-Ostwal proposes it as a short-term solution.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/718#issuecomment-2817075062) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue arises from how CrewAI handles custom embeddings when an embedder is provided within the crew. CrewAI manages this internally. However, the tools being used rely on Embedchain, which powers the RAG tool. Embedchain doesn't appear to support custom models, leading to the encountered problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2642#issuecomment-2817037446) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested that a proposed solution should ideally be effective. They believe the suggested method holds promise and is likely to produce the desired outcome. While not explicitly stating certainty, Vidit-Ostwal expresses confidence in the solution's potential. Their comment conveys a positive outlook, indicating that the suggested approach is*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2647#issuecomment-2817035431) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the configuration of the `planning_llm` that resolves the issue, specifically inquiring about the settings used. They provided an example configuration using the "openai/sabia-3" model with specific parameters like temperature, base URL, and API key. Vidit-Ostwal has requested confirmation on whether the defined LLM is compatible with*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2645#issuecomment-2817032826) in [crewAIInc/crewAI] on 2025-04-20.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the usage of the LLM class within CrewAI, pointing out that CrewAI provides its own LLM class that should be utilized when working with a crew. The suggestion references the CrewAI documentation regarding LLMs, specifically the Google section. They also propose implementing a validation check during*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2421#issuecomment-2816831311) in [crewAIInc/crewAI] on 2025-04-19.
  > *AI Summary: @Vidit-Ostwal has suggested expediting the merging process. The comment emphasizes the importance of moving forward with the integration. It underscores the need for prompt action and signals a readiness to incorporate the changes into the main codebase. The suggestion aims to streamline the workflow and facilitate the incorporation of recent*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2307#issuecomment-2816829318) in [crewAIInc/crewAI] on 2025-04-19.
  > *AI Summary: Vidit-Ostwal has suggested that the issue might stem from ChromaDB's behavior of locking a collection to the dimensionality of the first added embeddings. After initial collection creation, it adapts to the dimensionality of the first batch of embeddings. Subsequent additions or queries must then adhere to this established dimensionality, which*
- [Commented](https://github.com/mindverse/Second-Me/issues/157#issuecomment-2816816529) in [mindverse/Second-Me] on 2025-04-19.
  > *AI Summary: Vidit-Ostwal has suggested clarifying the appropriate action to resolve an issue. Specifically, they inquire whether resetting the memory would suffice to fix the problem. Alternatively, they ask if a more drastic measure, such as deleting the entire data folder and restarting the process from the beginning, is necessary. The question*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2616) in [crewAIInc/crewAI]: [BUG] Broken Test Case (2025-04-16).
  > *AI Summary: @Vidit-Ostwal has suggested there's a broken test case in the `test_mem0_storage.py` file, which can be reproduced by running it via `pytest`. The error encountered is an `OpenAIError`, indicating the OpenAI API key isn't being properly set. The test case should ideally pass without any errors. The issue arises during the*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2610) in [crewAIInc/crewAI]: Branch 2379 (2025-04-15).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2379. This resolves a problem identified and tracked under that specific issue number. The proposed solution addresses the core concern raised, aiming to rectify the reported behavior or deficiency. The contribution seeks to improve the overall functionality or stability related to the area*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2580) in [crewAIInc/crewAI]: Fix Mistral Issue: (2025-04-10).
  > *AI Summary: Vidit-Ostwal has suggested a fix for issue #2571. The primary focus is resolving an identified problem. The proposed solution addresses the root cause of the mentioned issue, aiming to eliminate the reported malfunction and ensure the system works as expected. This corrective measure enhances the system's reliability and stability by*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2570) in [crewAIInc/crewAI]: added condition to check whether _run function returns a coroutine ob… (2025-04-10).
  > *AI Summary: Vidit-Ostwal has suggested a resolution for issue #2538. The comment indicates a fix has been implemented to address the problem described in the referenced issue. The provided contribution aims to resolve the underlying causes or symptoms of the issue. This fix is intended to improve the functionality or stability of*
- Opened a [PR](https://github.com/crewAIInc/crewAI-tools/pull/251) in [crewAIInc/crewAI-tools]: Added Human Input from CLI (2025-03-31).
  > *AI Summary: @Vidit-Ostwal has suggested adding functionality to incorporate runtime data from Human through the command-line interface. This enhancement aims to provide a more direct method for integrating real-time human-generated information into the system. The initial implementation focuses on establishing a solid foundation for this data integration. Future development plans involve expanding*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2484) in [crewAIInc/crewAI]: Added test case for Issue #2260 (2025-03-26).
  > *AI Summary: Vidit-Ostwal has suggested adding a test case related to issue #2260. The suggestion aims to ensure that a specific scenario described in the linked issue is properly handled and validated. By including this test, the contributor intends to enhance the project's test suite, thereby improving its overall reliability and robustness.*

## ⭐ Starred Repositories
- Starred [google/A2A](https://github.com/google/A2A) on 2025-04-18.
- Starred [google/A2A](https://github.com/google/A2A) on 2025-04-15.
- Starred [github/github-mcp-server](https://github.com/github/github-mcp-server) on 2025-04-06.
- Starred [afshinea/stanford-cme-295-transformers-large-language-models](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models) on 2025-04-02.
- Starred [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) on 2025-03-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI-tools](https://github.com/Vidit-Ostwal/crewAI-tools) on 2025-03-31.
