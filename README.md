# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback from @jjmachan and @dosu to validate if the current solution is correct.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that a specific condition in the code, which checks if the variance of input tensors `var_x` and `var_y` is less than a specific bound, is the cause of unexpected behavior. The suggestion is based on the observation that the condition is met and a warning is raised*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested modifying the task 2 description to remove specific parameter references. Instead, the description should indicate that task 2 uses the output from task 1 without specifying the parameters. This change is recommended because the error in `interpolate_inputs_and_add_conversation_history()` arises due to the absence of a required parameter, 'detail,'*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the trace functionality to include `{prompt_number} : {trace}` for better organization. The new traces will be formatted as follows: `{'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Eifel tower is in Paris'), 'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])}, 'prompt_2': {'name': 'n_l_i_statement_prompt', 'input': NLIStatementInput(context='Paris, France is a city where Eifel tower*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal suggests modifying the flow to enhance user comprehension, which is deemed feasible from an implementation standpoint. If the suggestion aligns with @jjmachan's insights, @Vidit-Ostwal will update the PR to reflect this change.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that @thinkcybercloud should share the code for the requested functionality within the comment thread for better understanding and collaboration.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2005#issuecomment-2624920068) in [crewAIInc/crewAI] on 2025-01-30.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue is working fine for them when tested with `crewai version = 0.100.0`. They have not provided any further context or details about the testing environment or specific steps taken.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1978#issuecomment-2621726512) in [crewAIInc/crewAI] on 2025-01-29.
  > *AI Summary: @Vidit-Ostwal suggests setting `output_log_file` to `True` when defining the crew to determine if the mail sending task is executing multiple times or if other agents are involved. Additionally, a pull request (#1985) has been created to enhance log readability by saving them in JSON format. @Vidit-Ostwal offers assistance with integrating*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1989#issuecomment-2619935488) in [crewAIInc/crewAI] on 2025-01-28.
  > *AI Summary: @Vidit-Ostwal suggests that developing features that do not align with the maintainers' vision is futile. They acknowledge facing latency issues due to multiple API hits and believe that addressing latency is crucial and inevitable for the maintainers. However, the approach to solving this issue, such as using Kafka, remains at*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1989#issuecomment-2619584422) in [crewAIInc/crewAI] on 2025-01-28.
  > *AI Summary: @Vidit-Ostwal has suggested addressing concerns related to the number of agents running concurrently. Currently, only one agent operates at a time, or two if they depend on each other. Until an agent completes its task, no other requests from production can be processed. Scaling more than 10 agents simultaneously is*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file for enhanced parsability. This addresses the issue raised in #1970, allowing for more in-depth analysis. @Vidit-Ostwal is willing to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the purpose of `use_vision set = True` when defining an agent. They inquire whether the screenshot is analyzed by the multimodal LLM or if it still relies on element scraping and decision-making. They have noticed that `use_vision = True` only saves a `.gif` file, but the*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to save logs as a JSON file. This feature can be enabled by setting output_log_file to True or providing a filename and setting save_as_json to True. The generated JSON file will contain an array of JSON events, making it convenient for parsing and analysis.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the `parse_run_traces` function to include the last 4 letters of the `run_id` of the trace. This modification ensures a unique key for every call, thereby enhancing the precision of the function.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the validate_samples functionality to include the identification of the specific indexed sample that is causing an issue. This enhancement will provide more detailed information about the problematic sample, enabling users to pinpoint the exact sample causing the error.*

## ⭐ Starred Repositories
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
