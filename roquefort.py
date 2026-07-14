
Command	Purpose
1 git rebase master	---Move your current branch to start from
                    the latest master and replay your commits.
2 git cherry-pick <commit-hash>	---Copy one specific commit from another
                                branch to the current branch
3 Command	HEAD moves?	Changes kept?	Staged?
git reset --soft HEAD~1	✅	✅	✅
git reset HEAD~1 (--mixed)	✅	✅	❌
git reset --hard HEAD~1	✅	❌	❌
4 What is HEAD?

HEAD is a special pointer.

It points to the branch you're currently on.
5 Instead of typing a long commit hash, you use a pointer.
go on