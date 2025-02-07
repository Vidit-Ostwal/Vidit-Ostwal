# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the `get_crew` functionality to make it a CLI command. This will directly link the CLI command with the current crew instance. @lorenzejay has already started working on this expansion.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might lie in the initialization of `short_term_memory` and `entity_memory` by `reset_memory_command` executed from the CLI. This is different from the initialization done in `crew.py`. The `reset_memory_command` might not work for custom initializations of these memories.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve any conflicts that may arise.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio should review the proposed code and provide feedback. They also asked for an opinion on whether this functionality would enhance the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @sahusiddharth checks if the issue is related to the previous unit test PR made by them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested you provide more information to improve understanding. Additionally, they believe the following adjustment might resolve the issue:
"This should work in my opinion."*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested an opinion from other contributors (@jjmachan and @dosu) on the correctness of an unidentified solution. No specific error messages, guidance, or code examples are included in the comment. The comment suggests that @Vidit-Ostwal is seeking external validation of their proposed solution.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior in your code is likely due to a specific condition being met, which raises a warning about instability in predictions due to near-zero variance in the input data. They tested with different input tensors and found that the unexpected behavior only occurred in*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the error in `interpolate_inputs_and_add_conversation_history()` is due to it attempting to find the `detail` parameter before crew kickoff, when `detail` is not present. To resolve this, @Vidit-Ostwal recommends modifying `task 2` to use the output from `task 1` without specifying the parameter. Instead, it should take the*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to include `{prompt_number} : {trace}`. This will improve the format of the traces to include both the prompt number and the trace itself. The new traces will provide a clearer view of the prompt and its associated trace.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the provided sample code examples in the documentation for using embeddings with various platforms, including Azure OpenAI, Google AI, Vertex AI, and Cohere, should be updated to replace the `model_name` parameter with `model`. This change would align with the actual input required by the embedder.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output log file. Currently, the log file is in a .txt format, which makes it difficult to parse and analyze. The JSON format would address this issue and also partially resolve bug #1970. @Vidit-Ostwal expresses willingness to contribute by submitting*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the utility of `use_vision set = True` when defining an agent. They inquire about the specific impact on the processing flow, whether it triggers multimodal LLM-based parsing of screenshots or falls back to element scraping. They also express uncertainty about the cost metrics available to verify*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal suggests resolving the memory reset issue reported in #2023. Additional changes are also required:

1. Eliminating the CLI command for memory reset.
2. Updating documentation.

@Vidit-Ostwal is willing to implement these changes if the solution aligns with the project's goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested an update to fix the documentation issue raised in issue #2030. The issue was preventing users from understanding how to use the feature. By addressing this issue, the revised documentation will enhance user comprehension and facilitate seamless feature utilization.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, users can specify output_log_file as True or provide a filename. They should also set save_as_json to True. The generated JSON file will contain an array of JSON events, facilitating parsing and manipulation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the parse_run_traces function to incorporate the last four characters of a run's ID. By doing so, each call now has a distinct key, ensuring uniqueness. This change guarantees that every call can be distinctly identified and accessed, enhancing the traceability and organization of the data.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to identify the indexed sample that triggers issues. This enhancement provides more precise information about the root cause of sample validation failures.*

## ⭐ Starred Repositories
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
