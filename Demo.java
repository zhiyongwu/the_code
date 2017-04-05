/*
 * Copyright (c) 2017 Rsvp Technologies Inc. All rights reserved.
 * Project name : RsvpBotServer
 * File name : DeviceHabitDB.java
 * Last modified : 17-3-27 上午11:05
 *
 */

package cn.rsvptech.data.db;

import cn.rsvptech.data.bean.Habit;
import cn.rsvptech.data.helper.DataBaseHelper;
import org.apache.commons.lang3.StringUtils;

import java.sql.Time;
import java.util.List;


/**
 * Created by wuzhiyong on 2017/3/27.
 */
public class DeviceHabitDB {

    public static Habit queryUserHabit(String deviceId, String action, int day) {
        return DataBaseHelper.queryObject(Habit.class, "device_id = ? and habit_action = ? and habit_weekend = ?", deviceId, action, day);
    }

    public static Habit querySingeleUserHabit(String deviceId, String action) {
        return DataBaseHelper.queryObject(Habit.class, "device_id = ? and habit_action = ?", deviceId, action);
    }

    public static List<Habit> queryUserHabitList(String deviceId) {
        return DataBaseHelper.queryObjectList(Habit.class, "device_id = ?", deviceId);
    }

    /**
     * @param deviceId
     * @param action
     * @param time
     * @param message
     * @param resId
     * @param day      0是工作日 1是周末
     * @return
     */
    public static int insertUserHabit(String deviceId, String action, Time time, String message, Integer resId, Integer day) {
        Habit habit = queryUserHabit(deviceId, action, day);
        int row;
        if (habit == null) {
            row = DataBaseHelper.insertObject("insert into device_habit (device_id,habit_action,habit_time,habit_message,habit_res,habit_weekend) VALUES(?,?,?,?,?,?)",
                    deviceId, action, time, message, resId, day
            );
        } else {
            StringBuilder sb = new StringBuilder("update device_habit set ");
            if (time != null) {
                sb.append("habit_time = ").append("'").append(time).append("',");
            }
            if (StringUtils.isNotBlank(message)) {
                sb.append("habit_message = ").append("'").append(message.replace("'", "''")).append("',");
            }
            if (resId != null) {
                sb.append("habit_res = ").append(resId).append(",");
            }
            sb.append("habit_weekend = ").append(day).append(",");

            if (sb.lastIndexOf(",") != sb.length() - 1) {
                return 0;
            }
            sb.replace(sb.lastIndexOf(","), sb.length(), "");
            sb.append(" where device_id = ? and habit_action = ?");
            row = DataBaseHelper.insertObject(sb.toString(), deviceId, action);
        }
        return row;
    }


    public static void main(String[] args) {
        Time s = Time.valueOf("12:23:37");
        System.out.println(s);

    }
}
