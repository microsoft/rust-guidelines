<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## All agent-generated APIs require human review (M-HUMAN-REVIEW) { #M-HUMAN-REVIEW }

<why>To ensure API coherence, and adherence to project standards.</why>
<version>0.1</version>

Agents can do a great job authoring APIs within minutes that would take you otherwise hours to complete, but they often do a poor job designing 'for the right thing', or silently drop requirements. 

Rust has the advantage over many other languages of a strong type system to force correctness at compile time, and to design APIs that are fast and hard to misuse. Good API design can greatly aid in forcing a correct implementation. 

However, as APIs also define contracts between you and your users, bad choices can have viral effects (e.g., compare M-AVOID-WRAPPERS, M-AVOID-STATICS) and cannot easily be verified. 

Before submitting major PRs or releasing new APIs you and/or other human reviewers must check that all guidelines and other requirements are adhered to, and that the overall API looks reasonable. 

In particular, ensure all public APIs follow these guidelines and M-UPSTREAM-GUIDELINES. You may use LLMs to point out where these guidelines are not met, but (until model fidelity improves) you cannot take your agent's word that the guidelines are met.



