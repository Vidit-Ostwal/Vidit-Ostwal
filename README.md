# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested providing more information to clarify the issue because the provided context is not clear enough to understand the problem. Additionally, they believe the implementation should work as intended based on their understanding.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested verifying if a proposed solution is correct. They have requested input from @jjmachan and @dosu, highlighting the need for peer review to validate the solution's accuracy.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior observed is specific to the particular input tensors used in the example. An analysis of the code reveals that it checks if the variance of the input tensors falls below a certain threshold, and if so, raises a warning about potential instability in*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested to fix the error in `interpolate_inputs_and_add_conversation_history()` by adding a description to `task 2` without specifying the parameter. Instead, the description should mention that `task 2` takes the output from `task 1` and performs a specific task. If there are multiple output parameters from `task 1`, the description*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to have `{prompt_number} : {trace}`. This will make new traces appear as: ``` {'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Eifel tower is in Paris'), 'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])}, ... 'prompt_4': {'name': 'n_l_i_statement_prompt', 'input': NLIStatementInput(context='Eifel tower is in Paris', statements=['Paris is a city in*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal suggests considering the user perspective to improve flow comprehension. From an implementation standpoint, the change is feasible. They request input from @jjmachan on whether to proceed with the solution and await their approval before updating the PR with the proposed modification.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that the code snippet should be shared in the comment thread for easy reference and review. This would allow others to quickly access the code without having to navigate to an external location.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2005#issuecomment-2624920068) in [crewAIInc/crewAI] on 2025-01-30.
  > *AI Summary: @Vidit-Ostwal has suggested that the code is working fine for them with `crewai version = 0.100.0`. This information may be useful in troubleshooting any issues or understanding the compatibility of the code with different versions of the `crewai` library.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1978#issuecomment-2621726512) in [crewAIInc/crewAI] on 2025-01-29.
  > *AI Summary: @Vidit-Ostwal suggests setting `output_log_file = True` when defining the crew to determine if the mail sending task is executing twice alone or if other agents are also being invoked. They have also created a PR (#1985) to enhance log readability by saving logs in JSON format and offer to assist*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1989#issuecomment-2619935488) in [crewAIInc/crewAI] on 2025-01-28.
  > *AI Summary: @Vidit-Ostwal has suggested that developing features that do not align with the maintainers' vision is futile. While they appreciate the proposed solution for resolving latency issues during high API traffic, they acknowledge that a more comprehensive solution, such as using Kafka, may ultimately be necessary. However, the approach and implementation*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format to the output_log_file, which currently uses a .txt format. This would make the log file parsable and address issue #1970 partially. They are willing to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested looking into the purpose of the `use_vision set = True` parameter when defining an agent. They are unsure of whether the screenshot goes to a multimodal LLM for parsing or if it still falls back to scraping elements. Additionally, they have not found any key differences in*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. This feature can be enabled by setting output_log_file to True or providing a file name and setting save_as_json to True. The generated JSON file will contain an array of JSON events. This feature makes it easier to parse*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the `parse_run_traces` function. The modification includes the last four characters of the `run_id` of the trace, ensuring a unique key for each call. This change enhances the function's ability to distinguish between different trace calls and improves the accuracy and reliability of trace processing.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested an enhancement to the validate_samples functionality to provide additional information about the specific indexed sample causing any issues. This change improves the diagnostic capabilities of the tool by enabling users to identify the root cause of validation failures more easily.*

## ⭐ Starred Repositories
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
