# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the functionality to include a `get_crew` feature. This would allow CLI commands to be directly linked to the current crew instance. By implementing this, the need for a separate `get_crew` function is eliminated, streamlining the process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be caused by discrepancies in how the `reset_memory_command` initializes `short_term_memory` and `entity_memory` when executed from the CLI compared to within `crew.py`. While `reset_memory_command` is suitable for initializing `long_term_memory` and `knowledge_memory`, it may not work correctly for `short_term_memory` and `entity_memory` if these have custom*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve some conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review the code and share their thoughts on whether the implemented functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that the current issue might be due to a previous unit test pull request made by @sahusiddharth. He requests him to check if that is the case.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested providing more information to clarify their confusion, as they are unable to understand the current explanation. They have also proposed a potential solution, indicating that it should work in their opinion.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has sought confirmation from @jjmachan and @dosu if the proposed solution is correct. The commenter has not provided any additional context or details regarding the solution.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior seen in the code may be due to a specific case of input tensors, as a different set of tensors did not exhibit the same behavior. The warning raised in the commented code is meant to alert users to potential instability in certain*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested a modification to the description of `task 2`. They propose removing the specific parameterization and simply stating that `task 2` should use the output from `task 1` as input. This change is intended to avoid errors related to missing parameters and to make the code more flexible.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to include both the prompt number and the corresponding trace, ensuring that each trace is clearly identified within the JSON structure. The updated traces are structured as `{prompt_number} : {trace}`, where the trace contains information such as the prompt name, input, and output.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has pointed out that in the provided code examples for the "Memory" concept in the CrewAI documentation, the input parameter for the embedder is "model" instead of "model_name". This is the case for all the examples, including those for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested that the output_log_file should have a JSON format in addition to the existing .txt format. This is because the .txt format cannot be parsed, making it less useful for analysis. The JSON format would address this issue and also partially resolve GitHub issue #1970. @Vidit-Ostwal is willing*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested that the purpose of `use_vision set = True` when defining an agent is unclear. They are unsure if it triggers multimodal processing of images or relies solely on scraping and element analysis. They also seek clarification on whether there's a cost metric to verify if multimodal image*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the reset memories issue reported in #2023. However, additional changes are required, including:

- Removing the CLI command for resetting memories
- Making documentation changes

@Vidit-Ostwal is willing to implement these changes if the proposed solution aligns with the project goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. The changes address the missing information and improve the clarity of the documentation, ensuring users have a comprehensive understanding of the feature's functionality.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a new feature to save logs as a JSON file when initializing the crew. By setting `output_log_file` to True or a file name and enabling `save_as_json`, the crew will generate a JSON file containing an array of JSON events. This feature simplifies log parsing and handling.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the `parse_run_traces` function to include the last 4 letters of the `run_id` of the trace. This modification is expected to generate a unique key for every call, ensuring uniqueness in identification.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to include information about the specific indexed sample causing any errors encountered during validation. This enhancement aims to provide more detailed insights into potential issues, allowing for easier identification and resolution.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
