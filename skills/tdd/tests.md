# Good and Bad Tests

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal
parts.

```typescript
// GOOD: Tests observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Characteristics:

- Tests behavior users/callers care about
- Uses public API only
- Survives internal refactors
- Describes WHAT, not HOW
- One logical assertion per test

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

```typescript
// BAD: Tests implementation details
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red flags:

- Mocking internal collaborators
- Testing private methods
- Asserting on call counts/order
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through external means instead of interface

```typescript
// BAD: Bypasses interface to verify
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GOOD: Verifies through interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

**Tautological tests**: Expected value restates the implementation, so the test
passes by construction.

```typescript
// BAD: Expected value is recomputed the way the code computes it
test("calculateTotal sums line items", () => {
  const items = [{ price: 10 }, { price: 5 }];
  const expected = items.reduce((sum, i) => sum + i.price, 0);
  expect(calculateTotal(items)).toBe(expected);
});

// GOOD: Expected value is an independent, known literal
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```

The same trap has two quieter forms: pasting whatever the code currently
returns as the expectation (a typo in the output becomes a pinned
requirement), and using the code's own constants as the oracle
(`expect(ids).toEqual(STAGES.map((s) => s.id))`). Write the expected value from
the spec or the user's words, as a literal.

**Prose and inventory tests**: Read a prompt, doc, skill file, CSS, `--help`
text, or build output and assert that a phrase is present, or pin a list of
exports or filenames. They fail on every rewording and pass when the behavior
the words describe is broken.

```typescript
// BAD: Pins prompt wording
test("prompt tells the agent to be brief", () => {
  expect(buildPrompt()).toContain("in fewer than 100 words");
});
```

Requirements about wording are checked by reading the diff. Tests check only
structure a machine consumes: frontmatter parses, a referenced file exists, a
package entry point resolves and exports what its consumer imports.

**Removal guards**: When behavior or text is removed, the removed thing stays
out of the tests too. An assertion like `expect(text).not.toContain("old
phrase")` or "retired route is gone" fails only if someone types the exact old
words back in. Delete the old tests instead, and delete code that only those
tests still use.
