# Requirement changes

Canonical policy for a user change during ticketing or implementation. `to-tickets`, `implement`, and `implement-spec` point here.

A user change at any stage is a new requirement, not a footnote. It has the same authority as an initial requirement stated during grilling. If the user says "change A to B", propagate it through every artifact that exists so far, in this order:

1. **Spec**: update the published spec on the tracker; add B, remove or update A.
2. **Tickets**: update or add tickets for B; remove stale tickets for A.
3. **Tests**: remove or rewrite tests for A; write tests for B.
4. **Implementation**: update the code.

During ticketing, only the spec and tickets exist yet; update the spec first, then the tickets.

For a direct implementation where no spec exists, the implementation issue is the record: update its requirement summary and validation plan in place of steps 1 and 2.

Work that already landed or shipped in an open pull request is affected work too: rewrite its tests and code through steps 3 and 4, update the pull request body and Evidence, and rerun the validation that the change invalidates before reporting done.
