# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- Commented in [explodinggradients/ragas](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2613215323) on 2025-01-24.
  > *AI Summary: @Vidit-Ostwal suggests the following: - Update the Ragas version. - To resolve the first error, replace `OverlapScoreBuilder` with `JaccardSimilarityBuilder`. - The second error is because the `rel_builder` was initialized incorrectly. The correct call should be `rel_builder = JaccardSimilarityBuilder(property_name="page_content", new_property_name="entity_jaccard_similarity")` without `key_name`. - This is because the sample nodes do not*
- Commented in [explodinggradients/ragas](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2612806612) on 2025-01-24.
  > *AI Summary: @Vidit-Ostwal has suggested that the output of the Named Entity Recognition (NER) model should be a list of strings, not a dictionary. They have reviewed the documentation and believe there may be an error. @Vidit-Ostwal suggests updating the documentation to reflect the correct output format.*
- Commented in [explodinggradients/ragas](https://github.com/explodinggradients/ragas/issues/1875#issuecomment-2612549639) on 2025-01-24.
  > *AI Summary: @Vidit-Ostwal has suggested improving the `validate_samples` function by raising an error that specifies which sample is invalid and its type. This will help users identify the problematic sample more easily. The proposed code modification raises a `ValueError` with a message indicating the index and type of the invalid sample.*
- Commented in [explodinggradients/ragas](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2610590240) on 2025-01-23.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue could arise because the **_"prompt_traces"_** dictionary uses the **_"prompt_trace.name"_** as the key, which is not unique when called more than once. To resolve this, @Vidit-Ostwal recommends appending the last four letters of the **_run_id_** to the key, ensuring uniqueness. This modification would result in*
- Commented in [explodinggradients/ragas](https://github.com/explodinggradients/ragas/issues/1865#issuecomment-2606619575) on 2025-01-22.
  > *AI Summary: @Vidit-Ostwal has suggested reading the documentation for migrating from Ragas v0.1 to v0.2 to help with the current issue. The documentation provides a detailed explanation of the migration process and instructions on how to upgrade to v0.2.*

## 🐛 Issues Raised
No issues raised recently.

## 🚀 Pull Requests
- Opened a PR in [explodinggradients/ragas](https://github.com/explodinggradients/ragas/pull/1879): Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the validate_samples functionality to provide more detailed error messages. The new functionality will specify which indexed sample is causing the issue, making it easier to identify and resolve problems.*

## ⭐ Starred Repositories
- Starred [explodinggradients/ragas] on 2025-01-24.

## 🍴 Forked Repositories
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
