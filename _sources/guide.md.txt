# Instructor guide


## Why we teach this lesson

Everyone should document their code, even if they're working alone.

These are the main points:
- Code documentation has to be versionnable and branchable
- Code documentation should be tracked together with the source code
- README is often enough

**Please do not skim over the two above points**. Please take few minutes to
explain why documentation (sources) should be tracked together with the source
code.  Please discuss this aspect with workshop participants and connect it to
**reproducibility**. This is for me (Radovan) the most important take-home
message.

Specific motivations:

- Code documentation becomes quickly unmanageable if not part of the source code.
- It helps people to quickly use your code thus reducing the time spent to explain over and again to new users.
- It helps people to collaborate.
- It improves the design of your code.


## Intended learning outcomes

By the end of this lesson, learners should:
- Understand the importance of writing code documentation together with the source code
- Know what makes a good documentation
- Learn what tools can be used for writing documentation
- Be able to motivate a balanced decision: sometimes READMEs are absolutely enough


## Timing

As an instructor you should prepare all bullet points but do not go through
each bullet point in detail. Only highlight the main points and rather give
time for a discussion. Leave details for a later lecture for those who want to
find out more. If you go through each bullet point in detail, the motivation
can easily take up 30 minutes and you will run out of time.

The lesson does not fit into 1.5 hours if you go through everything. Optimize
for discussions and prepare well to be able to jump over bullet points which
can be left for a later lecture. Some sections can be skipped if needed (see
below). However, we recommend to have a discussion with your learners to make
them aware of what the training material contains.

- Do not insist on practicing Markdown or RST syntax.
- The section *Rendering (LaTeX) math equations* may be optional if your
  attendees do not have to deal with equations.
- In the GitHub Pages episode, the
  goal is not anymore to write code documentation but to show how to build
  project website with GitHub. If time is tight, the GitHub pages episode can be
  skipped or can be done as demonstration instead of exercise.


## Detailed schedule

- 09:00 - 09:10 Motivation and tools
  - create a wishlist in collaborative notes
- 09:10 - 09:20 Writing good README files
  - brief discussion
- 09:20 - 09:40 **Exercises**: README-1, README-2, README-3 (choose one or multiple)
- 09:40 - 10:00 Sphinx and Markdown: Sphinx-1 as type along

- 10:00 - 10:10 Break

- 10:10 - 10:40 **Exercises**, Sphinx-2, Sphinx-3, GH-Pages-1
- 10:40 - 11:00 Discussion, GH Pages, Summary


## Place this lesson towards the end of the workshop

Reason is that with collaborative Git we can create more interesting
documentation exercises. Currently there are some elements of forking and
pushing and this is only really introduced on day two.  We have tried this
lesson on day one and it felt too early and disconnected/abrupt.  It works best
after the reproducibility lesson since we then reuse the example and it feels
familiar.


## Troubleshooting

### Character encoding issues

Can arise when using non-utf8 characters in `conf.py`. Diagnose this with `file -i conf.py`
and `locale`.


## Live better than reading the website material

It is better to demonstrate the commands live and type-along. Ideally connecting
to examples discussed earlier.

In online workshops most of the type-along becomes group exercise work where groups
can share screen and discuss.


## Field reports

### 2022 September

We were pressed for time (we started 5-10 minutes late, relative to
the schedule below), so we made most of the first lessons fast.  In
the schedule below, note that we had the first 10 minutes for
"Motivation" *and* "Popular tools", which we didn't fully realize so
that put us even further behind.  Doing these introduction
parts quickly was hard but was probably worth it since we had plenty
of time in the end.  For the "tools", one person summarized the point
of each section on the page quickly.  The README episode was done
quickly, we basically skipped the exercises to get to Sphinx, and this
put us back on schedule.

For Sphinx, we did it a lot like you see in the schedule: first
exercise (the basic setup) was type-along, but it was a bit too much
to do in the 10 minutes we had allotted (we typed too fast).  But,
people then had a nice long time to make it up and do everything.  It
seemed to work well.  The GitHub pages deployment could then be done
as a nice, slow demo, and we had plenty of time to ask questions.

Overall, I think this was the right track, but we could have practiced
doing the first parts even faster, and warned people that we focus on
the Sphinx exercises.
