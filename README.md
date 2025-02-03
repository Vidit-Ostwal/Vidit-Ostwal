# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback from @jjmachan and @dosu on the correctness of their proposed solution. However, the specific details of the solution are not provided in the comment.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior is unique to the input tensor. After analyzing the code, they identified a specific condition that triggers a warning when the variance of predis is close to zero. This condition can lead to incorrect correlation coefficient results. To address this issue, they recommend*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the error in `interpolate_inputs_and_add_conversation_history()` is due to it trying to find the `detail` parameter before the crew kickoff. They recommend adding a description to `task 2` to clarify that it should use the output of `task 1` without explicitly setting parameters. This would resolve the issue*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to include "prompt_number: {trace}" for new traces. The updated traces would resemble this format:

```
{'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Eifel tower is in Paris'), 'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])}, ...}
```*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested that the approach @VladTabakovCortea is suggesting makes sense from the user's perspective, as it would simplify the flow's comprehension. @Vidit-Ostwal believes it should be straightforward to implement from a technical standpoint. @Vidit-Ostwal has requested @jjmachan's input to confirm the alignment with this solution. If @jjmachan approves, @Vidit-Ostwal*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested introducing a JSON format for the output log file, allowing for easier parsability and analysis. They believe this will partially address the limitations of the current .txt format. They have expressed willingness to contribute to the implementation by submitting a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal suggests clarifying the purpose of the `use_vision` parameter when defining agents, specifically its impact on how screenshots are processed. This parameter controls whether the multimodal LLM is used to interpret screenshots or if traditional scraping and element-based analysis is performed. The key visible difference with `use_vision = True` is*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. To do this, set `output_log_file` to `True` or a file name like `"log.json"` and set `save_as_json` to `True`. This will create a JSON file containing an array of JSON events, simplifying parsing and working with the logs. An*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the parse_run_traces function to include the last 4 letters of the trace's run_id. This results in a unique key for every call, which should improve the accuracy of the function.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the `validate_samples` functionality to provide information about the specific indexed sample that is causing issues. This change will help identify the problematic sample more easily.*

## ⭐ Starred Repositories
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
