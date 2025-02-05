# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve some conflicts. This will help ensure that the changes are merged smoothly and any potential issues are addressed.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review the provided code and share their thoughts on it. Additionally, @Vidit-Ostwal has asked whether this functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be related to a previous unit test pull request made by @sahusiddharth. They have requested @sahusiddharth to verify if this is indeed the cause.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal suggests clarifying a confusing aspect of the code. They believe that the code should function as expected, but request additional information to better understand the issue. They have offered their opinion on the code's expected behavior, expressing that it should work as intended.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested a review from @jjmachan and @dosu on the provided solution. They are asking if the solution is correct and would appreciate feedback.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior observed may be specific to the particular case due to the variance of the input tensor being close to zero. This condition triggers a warning to highlight potential instability in correlations, leading to incorrect results. They recommend considering input rescaling or using a*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested modifying the description of `task 2` to include the necessary dependencies without explicitly setting parameters. Instead, it should indicate that `task 2` utilizes the output from `task 1`. This modification eliminates the error that occurred due to the absence of the `detail` parameter in the `interpolate_inputs_and_add_conversation_history()` function,*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updates to the traces functionality to include `{prompt_number} : {trace}`. This will result in traces appearing as a dictionary where each key represents a prompt number and the corresponding value is a dictionary containing the prompt name, input, and output. This new format provides a structured and*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested considering the user's perspective and making the flow easier to understand. They believe it's feasible from an implementation standpoint and have requested @jjmachan's input before updating the PR with this change.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the code for the discussed functionality within the current thread. This would enable easy reference and code review for all participants.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for CrewAI's memory concept contains errors in its sample code examples. Specifically, the embedder takes input of "model" instead of "model_name." They have provided specific links to the documentation pages where these errors can be found.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format support to the logging file, as the current .txt format is not parsable. This JSON format would enable further analysis and partially address issue #1970. They are willing to contribute a pull request for this implementation.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the purpose of `use_vision set = True` when defining an agent. He questions if the screenshot is processed by the multimodal LLM or if scraping and element-based decision-making are still used. Vidit has observed that the only noticeable difference with `use_vision = True` is the saving*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue discussed in issue #2030. The changes address the reported discrepancies and improve the clarity and accuracy of the documentation. The suggested modifications enhance the overall reliability and usability of the documentation for users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a new feature to save logs as a JSON file. When initializing the crew, users can set `output_log_file` to a file name (e.g., "log.json") and enable `save_as_json` to True. This will create a JSON file containing an array of JSON events, which can be easily parsed*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the parse_run_traces function. The change involves incorporating the last 4 characters of the run_id into the trace, resulting in a unique key for each call. This modification ensures that each call has a distinct identifier.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to provide more detailed error messaging. The updated functionality will specify which indexed sample is causing the issue, making it easier to identify and resolve the problem. This enhancement will improve the user experience by providing more specific error information.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
