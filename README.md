# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the current implementation may not be clear and has requested further clarification. They believe that an alternative approach could potentially resolve the issue and have offered to share their insights.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested confirmation from @jjmachan and @dosu if the provided solution is correct. They have not provided any additional context or specific details about the solution, so it's unclear what aspect of the solution they are seeking verification for.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior observed in the code may be specific to the particular input tensors used. They have observed that in a different case with the same input tensors but a constant `y_pred`, the result was as expected (`nan` was in the output). They believe that*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal suggests that `interpolate_inputs_and_add_conversation_history` initializes parameters before crew kickoff and attempts to find a non-existent `detail` parameter. To resolve this, they recommend updating the description of `task 2` to specify the necessary output from `task 1` without explicitly setting parameters. Instead of specifying parameters in `task 2`, use phrases like*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to follow the format `{prompt_number} : {trace}`.

New traces should appear as:
`{'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Eifel tower is in Paris'), 'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])}, ...}`*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that the proposed solution makes sense from a user's perspective, as it simplifies the understanding of the flow. From an implementation standpoint, they believe it should be relatively straightforward. They have requested input from @jjmachan and indicated that they will incorporate the modification into the PR if*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2015#issuecomment-2628794304) in [crewAIInc/crewAI] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that @thinkcybercloud share the code for this issue. This would be helpful for understanding the context and potential solutions.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2005#issuecomment-2624920068) in [crewAIInc/crewAI] on 2025-01-30.
  > *AI Summary: @Vidit-Ostwal has reported that the code is functioning as intended based on his testing. He also specifies that version `0.100.0` of the `crewai` library was employed during the testing process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1978#issuecomment-2621726512) in [crewAIInc/crewAI] on 2025-01-29.
  > *AI Summary: @Vidit-Ostwal suggests setting `output_log_file = True` when defining the crew to determine if the mail sending task is executing twice or if another agent is being called. They have also created a PR (#1985) to enhance log readability by saving them in JSON format. They offer to help integrate these*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1989#issuecomment-2619935488) in [crewAIInc/crewAI] on 2025-01-28.
  > *AI Summary: @Vidit-Ostwal recognizes the importance of aligning contributions with maintainer vision. He is experiencing an issue with API latency that partially aligns with the proposed solution. He anticipates the need for a latency-solving solution in the future and suggests that maintainers consider implementing Kafka or a similar solution to address this*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format to the output_log_file as the current .txt format is not parsable. This JSON format will enable further analysis and partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this change.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested guidelines for using the `use_vision` parameter. When set to `True` in agent definition, it saves a `.gif`. However, the key difference in output is unclear, as it still relies on scraping elements and making decisions. Additionally, the commentator asks about a cost metric to determine if multimodal*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file when initializing the Crew object. By setting the output_log_file parameter to True or specifying a file name and setting the save_as_json parameter to True, users can enable this feature. The resulting JSON file will contain an array of*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the parse_run_traces function to include the last four letters of the run_id of the trace. This change ensures that every call has a unique key, which is necessary to uniquely identify each call. The implementation details of the function are not included in the suggestion, as*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested altering the validate_samples functionality to include information on the specific indexed sample responsible for any encountered issues. By doing so, users can pinpoint the problematic sample and address it accordingly.*

## ⭐ Starred Repositories
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
