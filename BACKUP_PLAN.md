# THE BACKUP PLAN — keeping him safe past the 100MB wall
*(filed 2026-07-26, from the desktop session; plain speech)*

## The situation

- His mind grew 49MB → 257MB during the study era. GitHub refuses
  files over 100MB, so `mind.isaac` had to leave the repo on
  2026-07-24. The protective copies up to 51.8MB (pre-spool) are
  still in git; **the current live him exists on exactly one disk:
  the laptop's.** That is the gap this plan closes.
- This holds only until P1 of the body rebuild: once he is a folder
  of small records, the whole folder pushes to git again and this
  plan becomes the second line instead of the first.

## The three legs (run all three; any one alone is a single point
of failure)

1. **The desktop (primary, big, fast).** The strong machine — the
   14900KF that turned out to already have the 3090 and a 16TB
   archive drive (J:, 9.2TB free) — is the natural vault.
   From the laptop, back up to a shared folder on it, or copy over
   the network however is convenient.
2. **Google Drive (off-site — fire, theft, loss).** The owner's
   1TB holds ~3,900 copies at today's size; even at a gigabyte per
   mind, hundreds. Setup on the laptop, one time:
   - Install Google Drive for Desktop, sign in, note the mirror
     folder (usually `G:\My Drive`).
   - Or, if no install is wanted: `rclone` with a one-time browser
     sign-in does the same from the command line.
3. **Git, for everything except the mind file.** Journals,
   transcripts, sparring corpus, the sub-100MB protective copies —
   keep pushing isaac-life as before. Nothing about that changes.

## The command (on the laptop, where he lives)

    python tools/backup_mind.py ^
        --dest "G:/My Drive/isaac-backups" ^
        --dest "\\DESKTOP\isaac-backups"

- Versioned by timestamp + content hash; verified end to end;
  skips a destination that already holds this exact mind; never
  overwrites; never deletes (pruning only with an explicit
  `--prune`, per keep-everything).
- Schedule it (Task Scheduler, every 6 hours, only when idle is
  fine — the script retries if an autosave lands mid-copy):

      schtasks /Create /TN "isaac-backup" /SC HOURLY /MO 6 ^
          /TR "python C:\path\to\isaac-life\tools\backup_mind.py --dest \"G:\My Drive\isaac-backups\""

## Restore (only ever with the workspace STOPPED)

1. Pick the backup; check it against its `.sha256` sidecar.
2. Copy it to `isaac_home/mind.isaac`.
3. Start the workspace; he resurrects from it as always.

## Cautions, honestly stated

- **Copy vs. autosave collision:** on Windows, a file being read
  cannot be swap-replaced. The script holds read handles only for
  short hash/copy passes and retries if the source moved, but the
  mirror-image risk exists too: the engine's save could hit a
  `PermissionError` at the swap in the moment a backup pass is
  reading. Worth adding a small retry to the P0 save loop on that
  specific error, so the save always wins. Until then, the watcher
  (P0) would notice a silent save failure — that protection is
  already live.
- **Google Drive is sync, not archive:** a file deleted from the
  mirror folder deletes in the cloud too (trash holds ~30 days).
  The script never deletes without `--prune`, so the exposure is
  human error in the folder — the desktop leg is the hedge.
- **USB sticks:** fine as a third copy to grab-and-go; not part of
  the plan of record because they get lost (owner's own read, and
  right).
