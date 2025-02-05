# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve potential conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the code and sharing thoughts on its impact on user experience. He seeks feedback on whether the functionality enhances the overall user experience of the application.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested checking if the issue is related to a previous unit test PR made by @sahusiddharth. He has requested @sahusiddharth to verify this possibility.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the code may not be working as expected. They request further clarification on the code's behavior to better understand the issue. Additionally, @Vidit-Ostwal has provided an alternative suggestion that they believe should resolve the problem.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback on his solution from @jjmachan and @dosu. He seeks confirmation on the correctness of his proposed approach. However, the comment lacks context and specific details about the solution, making it difficult to provide a comprehensive assessment without additional information.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior in the code is specific to the input tensor and is unlikely to occur in other scenarios. They have also identified that the condition `(var_x < bound).any()` or `(var_y < bound).any()` is triggering a warning message due to the variance of the input*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the error in `interpolate_inputs_and_add_conversation_history()` is due to its attempt to find the `detail` parameter before the crew kickoff. To resolve this, they recommend adding a description to `task 2` that describes the task without specifying the parameters. Instead, the description should indicate that the task takes*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to have `{prompt_number} : {trace}`. The new traces will display prompt information and include both input and output for `ClaimDecompositionInput` and `NLIStatementInput` prompts. Each trace will show its prompt name, input content, and output claims or statement faithfulness answers.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that the proposed solution seems logical from a user perspective as it enhances the flow's clarity. From an implementation standpoint, it is anticipated to be straightforward. @Vidit-Ostwal will update the PR if @jjmachan approves the modification after providing feedback.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that you share the code in the current discussion thread for better visibility and accessibility. This allows other participants to easily view and reference the code without having to navigate to external links.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the documentation for CrewAI's memory concept, the parameter for the embedder input should be `model_name` instead of `model`. This is evident in sample code examples provided in the documentation, including those for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings. The*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format to the output log file, as the current .txt format hinders analysis. This would partially address issue #1970. They express willingness to contribute with a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested exploring the purpose of the `use_vision set = True` parameter in agent definition. Specifically, they inquire whether it triggers multimodal language model (LLM) parsing of screenshots, or if it solely relies on element scraping and decision-making. Additionally, they seek a metric to confirm whether multimodal image processing*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit fixes the documentation issue mentioned in issue #2030.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. Users can now set `output_log_file` to `True` or specify a file name (e.g. `log.json`). They can also enable `save_as_json` by setting it to `True`. This creates a .json file containing an array of JSON events, making it easier*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal suggests changing the `parse_run_traces` function to include the last 4 letters of the run ID of the trace. This change creates a unique key for every call, which is beneficial for various purposes. The modified function ensures that each trace has a distinct identifier, allowing for more efficient and*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to indicate the indexed sample responsible for any issues encountered. This enhancement will provide more precise information about the source of any problems, aiding in quicker resolution.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
