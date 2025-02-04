# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested discussing further as they are facing difficulty in understanding the provided solution. They believe an alternative solution may be more effective and have shared their thoughts on a potential approach.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback on the provided solution. They have not provided any details or context regarding the solution, so it is not possible to evaluate its correctness.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behaviour encountered is likely specific to the particular input tensor being used. After reviewing the code, they have identified that a condition in the code will trigger a warning if the variance of the input tensors is close to zero. They have suggested that*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested modifying `task 2` in the following way: - The function `interpolate_inputs_and_add_conversation_history()` should be initialized before the crew kickoff. - Remove the direct reference to the `detail` parameter from the `task 2` description. - Instead, specify that `task 2` should use the output of `task 1`, or take*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to display `{prompt_number} : {trace}`. These traces should look like: `{'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Eifel tower is in Paris'), 'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])}, 'prompt_2': {'name': 'n_l_i_statement_prompt', 'input': NLIStatementInput(context='Paris, France is a city where Eifel tower is located', statements=['Eiffel tower is in*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested implementing a change that simplifies the understanding of the flow for users. From the implementation perspective, this change is considered feasible. @Vidit-Ostwal will proceed with updating the PR with this modification if @jjmachan approves the solution.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that you share the code for this issue here for easier reference and collaboration. This will allow other contributors to quickly understand the context and provide their input or suggestions. Sharing the code here will facilitate a more efficient and streamlined discussion.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2005#issuecomment-2624920068) in [crewAIInc/crewAI] on 2025-01-30.
  > *AI Summary: @Vidit-Ostwal has suggested that the code is working fine for them. They have also mentioned their `crewai` version as 0.100.0.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1978#issuecomment-2621726512) in [crewAIInc/crewAI] on 2025-01-29.
  > *AI Summary: @Vidit-Ostwal has suggested setting `output_log_file = True` when defining the crew to determine if the mail sending task is executing twice or if other agents are being called. Additionally, they have created a PR (#1985) to enhance log readability by saving them in JSON format. @Vidit-Ostwal has offered to assist*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1989#issuecomment-2619935488) in [crewAIInc/crewAI] on 2025-01-28.
  > *AI Summary: @Vidit-Ostwal has suggested investigating the problem of API latency when handling multiple hits. @alm0ra's proposed solution partially addresses the issue. @Vidit-Ostwal believes addressing latency issues through bug fixes or feature requests is inevitable and requires maintainers' attention. The approach to solving this problem, whether through Kafka or other means, is*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file. Currently, the file is in .txt format, which limits its parsability and analysis capabilities. The JSON format would address this issue and partially fulfill the request in issue #1970. @Vidit-Ostwal expresses willingness to contribute a pull request for this*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifications regarding the use of `use_vision` parameter when defining an agent. This parameter determines if the agent should use image recognition for decision-making. When set to `True`, the agent will use both image recognition and element scraping for decision-making. However, the difference between using `use_vision=True` and `use_vision=False`*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. This feature simplifies the process of parsing and working with the logs. To utilize this feature when initializing the crew, simply set output_log_file to True or specify a file name and enable save_as_json. The generated .json file will*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the parse_run_traces function to include the last 4 letters of the trace's run_id. This change creates a unique key for each call, ensuring uniqueness and potentially improving the function's operation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the validate_samples functionality to additionally identify the indexed sample responsible for any discrepancies. This enhancement aims to provide more specific information and facilitate troubleshooting processes.*

## ⭐ Starred Repositories
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
