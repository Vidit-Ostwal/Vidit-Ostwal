# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback from @jjmachan and @dosu on the validity of the proposed solution.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior in your code may be due to a specific condition that arises from the variance of the input tensors being close to zero. They identified the following code block as potentially relevant: ``` bound = math.sqrt(torch.finfo(var_x.dtype).eps) if (var_x < bound).any() or (var_y <*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that moving the initialization of parameters to `interpolate_inputs_and_add_conversation_history()` function will resolve the error in the code. This error is caused by the absence of the required parameter `detail` before the crew kickoff. To resolve this, @Vidit-Ostwal recommends modifying the description of `task 2` to remove explicit parameter*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to display `{prompt_number} : {trace}`. New traces will be structured as follows: {`prompt_1`: `{name: 'claim_decomposition_prompt', input: {response: 'Eifel tower is in Paris'}, output: {claims: ['Eiffel tower is in Paris.']}}`, `prompt_2`: `{name: 'n_l_i_statement_prompt', input: {context: 'Paris, France is a city where Eifel tower is*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that, from a user's perspective, the proposed flow is simple and understandable. It would also be easy to implement. @Vidit-Ostwal is awaiting input from @jjmachan for further guidance. If approved, @Vidit-Ostwal will update the PR with the suggested modification.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the output logging file, currently in .txt format, to support JSON format. This improvement will facilitate data parsing and analysis and partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request with this change.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the purpose of the `use_vision` parameter when defining an agent. They inquire about whether enabling this parameter redirects image processing to the multimodal LLM or if it still relies on element scraping. Additionally, they ask if there are cost metrics to determine if multimodal image processing*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file when initializing the crew. By setting output_log_file to True or providing a filename and setting save_as_json to True, users can generate a .json file containing an array of JSON events. This simplifies parsing and working with the logs.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal suggests changing the parse_run_traces function to include the last four letters of the run_id of the trace. This ensures that every call has a unique key, preventing duplicates and improving overall accuracy.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested changing the validate_samples functionality to additionally indicate which indexed sample is causing the problem. This modification will enhance the functionality of validate_samples by providing more specific information about the source of the issue, allowing for more efficient debugging and troubleshooting.*

## ⭐ Starred Repositories
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
