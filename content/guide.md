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

- **00:00 - 00:10 Motivation and wishlist**
  - create a wishlist in collaborative notes
- **00:10 - 00:18 Popular tools and solutions**
  - Note: it starts with in-code documentation, do not waste much time on this since there's a discussion following right after
- **00:18 - 00:25 In code documentation**
- **00:25 - 00:50 Writing good README files**
  - 00:25 - 00:30 brief discussion
  - 00:30 - 00:35 **Walkthrough:** README-1, opening an empty project on GitHub, with a README, and copy-pasting code from the teaching material and using the preview
  - 00:35 - 00:45 **Exercises**:  README-2, README-3 (choose one or multiple). 
    We propose [https://github.com/opendatalab/MinerU](https://github.com/opendatalab/MinerU)
    to have something to discuss 
  - 00:45 - 00:50 Discussion of exercises and the notes
- 00:50 - 01:00 Break
- **01:00 - 01:40 Sphinx and Markdown**
  - 01:00 - 01:15 **Type along**: Sphinx-1
  - 01:15 - 01:35 **Exercises**: Sphinx-2/3/4 
  - 01:35 - 01:40 Discussion 
- **01:40 - 02:00 Sphinx deploy on GitHub**
  - **Type along**: GH-Pages 1 
- 02:00 - 02:10 Break
- **02:10 - 02:20: Walkthrough Personal/Project Home Page on GitHub**
- **02:20 - 02:30: Discussion and summary** 


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
