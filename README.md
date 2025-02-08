# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2055#issuecomment-2643704539) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may have been resolved. They recommend updating the crew version and have provided a link to PR #2055 for further details.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2643616523) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests evaluating CrewAI's outputs, agent performance, and task results. Built-in evaluations would assess factual accuracy and task-specific criteria. This concept is inspired by the work RAGAS does in structured evaluations for retrieval-augmented generation. He wants to understand how such evaluations could be incorporated into CrewAI.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests expanding the code to include a `get_crew` functionality that could be linked directly to the current crew instance through a command-line interface (CLI). They acknowledge that they initially overlooked this idea and commend the user (@lorenzejay) for suggesting it.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may arise from the different initialization methods used for `short_term_memory` and `entity_memory` when executing `reset_memory_command` from the CLI compared to `crew.py`. They highlight that the direct CLI command may not work if any custom initialization is performed for these memories, as they require arguments*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve any conflicts that may arise in completing the task.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the commit's code and providing feedback on its merits. Additionally, they have requested an assessment of whether the implemented functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that it be checked if the issue is caused due to a previous unit test PR by @sahusiddharth.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested considering the following improvements:

- Provide additional details or explanations to clarify the concern or misunderstanding.
- Offer suggestions or alternatives that might address the issue and improve understanding.
- Rephrase or simplify the language used in the original statement to make it more accessible.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal inquired about the correctness of a solution he proposed in the discussion. He referred to users @jjmachan and @dosu for their expertise and validation on the accuracy of his approach.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be due to unexpected behavior in the provided code. They analyzed the code and identified a specific condition that triggers a warning related to variances being close to zero. They tested with different input tensors and observed that the issue seems to be*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the CrewAI documentation for memory concepts is incorrect. In the sample code examples provided, the `embedder` takes the input of `model` instead of `model_name`, as stated in the docs. This issue is present in multiple sections of the documentation, including those for Azure OpenAI, Google AI,*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format to the logging file for better parsability. This would also partially address issue #1970. They have expressed willingness to contribute by submitting a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested providing more information about the `use_vision` flag when defining an agent. They have noted that when `use_vision` is set to True, a .gif is saved, but the output remains the same. They have questioned whether setting `use_vision` to True triggers multimodal processing of images and if there*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the memories reset issue raised in #2023. Their solution involves:

- Eliminating the CLI command responsible for resetting memories
- Updating the documentation to reflect these changes

@Vidit-Ostwal has expressed a willingness to implement these adjustments if the proposed solution aligns with the overall goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the documentation issue that was mentioned in issue #2030. This issue affected the documentation, and the proposed fix will resolve the specific problem that was causing it. @Vidit-Ostwal's suggestion aims to enhance the accuracy and clarity of the documentation, ensuring that it accurately reflects the functionality*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. Users can now set the output_log_file parameter to True or a file name (e.g., "log.json") and enable save_as_json to True when initializing the crew. This generates a .json file containing an array of JSON events.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the `parse_run_traces` function to generate a unique key for every call by including the last four letters of the trace's `run_id`. This change ensures that each call has a distinct identifier.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested changing the `validate_samples` functionality to provide information on which indexed sample is causing an issue. This update will enhance the tool's diagnostic capabilities by pinpointing the specific sample responsible for any problems, enabling more efficient troubleshooting and resolution.*

## ⭐ Starred Repositories
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
