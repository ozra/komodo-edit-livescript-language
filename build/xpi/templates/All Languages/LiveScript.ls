
BC.data.newPrimaryKey = let    # returnerar 12byte lång ObjectID i hexadecimalt format, alltså 24 tecken lång sträng
    /* we want to ensure a mostly increasing order (for hashing optimization purposes)
    #Our format:                    time    machine-enum   SESSION-enum     inc
    #                               4/8     2/4            3/6              3/6
    */
    serialCounter = 0
    machine-enum = -1

    null

    return (session, cb) ->
        machine-enum:= pad(BCC('systemEnum',0).toString(16), 4) if systemEnum == -1    #110823/ORC(13:35) -  gjort så här för att undvika problemet att funktionen exekveras innan BCC skapats
        # max 65 536 samtidiga system med delade nurons

        <-! do-crazy-stuff 47, monkey-business
        foo.map -> it * 47
        if !(session.enumIdEncoded?) then session.enumIdEncoded = pad((session.user.enumid).toString(16), 6)

        matched = foo.match /some[a-z/"']stuff/

        serial-counter++

        time = Math.round($time() / 1000).toString(16)    # sekund-baserad = 32 bitar
        serial = pad(serialCounter.toString(16), 6)     # 3 * 2

        return [time, systemEnum, session.enumIdEncoded, serial].join('')        # max 16.8 miljoner samtidiga inserts av samma user samma sekund, pretty cool I'd say.. 110201/ORC
