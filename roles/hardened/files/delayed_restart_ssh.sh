#! /bin/bash
# Safety script to restart ssh in t + 10secs
# Designed to be run *before* editing the PAM requirements, otherwise a risk
# that we lock ourselves out of the syste. Little bit hacky...
# run with ssh host < delayed_restart_ssh.sh

TIME=10

# Debug, prove this executes after we disconnect
rm $HOME/.delayed_restart_ssh

echo -e '\nRestarting ssh in $TIME seconds'
CMD="sleep $TIME; touch $HOME/.delayed_restart_ssh; service ssh restart"
$CMD &  # run in background so andsible disconnects and moves on in parallel

# alternatively run this locally and then have script delete itself
rm -- "$0"
